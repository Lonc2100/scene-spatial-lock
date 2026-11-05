from pathlib import Path
import argparse,json,hashlib

def compile_scene(scene,out):
    out=Path(out);image=Path(scene['reference_image']);assert image.is_file()
    anchors=scene['anchors'];ids=[x['id'] for x in anchors]
    if not anchors or len(ids)!=len(set(ids)):raise ValueError('Nonempty unique anchors required')
    if any(x['evidence'] not in ['visible','author','convention'] for x in anchors):raise ValueError('Unknown structure must not become a fixed anchor')
    if not scene['axis_lock'] or 'unknown_regions' not in scene:raise ValueError('Axis and explicit unknown-region list required')
    mode=scene.get('axis_mode','declared_in_text')
    if mode not in ['declared_in_text','same_side','reverse_views']:raise ValueError('Unknown axis mode')
    views=[Path(p) for p in scene.get('view_references',[])]
    if any(not p.is_file() for p in views):raise FileNotFoundError('View reference missing')
    if mode=='reverse_views' and len(views)<2 and not scene.get('back_view_basis','').strip():raise ValueError('Reverse views require two reference images or explicit author back-view basis')
    if (out/'空间锁提示词.txt').exists():raise FileExistsError('Use a new output version')
    facts='；'.join(x['name']+'：'+x['relation'] for x in anchors)
    body='空间锁：'+scene['time_place']+'。'+facts+'。'+scene.get('route','人物与路线：未提供，本段不作推断。')+scene.get('light','')+scene.get('state_locks','')
    axis='摄影机轴线锁：'+scene['axis_lock']
    unknown='\n\n未确定的画外区域：'+'；'.join(scene['unknown_regions']) if scene['unknown_regions'] else ''
    text=body+'\n\n'+axis+unknown
    out.mkdir(parents=True,exist_ok=True);(out/'空间锁提示词.txt').write_text(text,encoding='utf-8')
    for shot in scene['shots']:
        if not shot['id'].isalnum():raise ValueError('Shot id must be alphanumeric')
        (out/(shot['id']+'_镜头提示词.txt')).write_text(text+'\n\n本镜机位：'+shot['camera']+'。'+shot['prompt'],encoding='utf-8')
    receipt=dict(scene=scene,skill_version='0.1.1',axis_mode=mode,reference_sha256=hashlib.sha256(image.read_bytes()).hexdigest(),view_reference_sha256=[hashlib.sha256(p.read_bytes()).hexdigest() for p in views],anchor_count=len(anchors),prompt_sha256=hashlib.sha256(text.encode()).hexdigest(),structure_check='passed',visual_understanding=scene.get('visual_review','未提供视觉审读记录；脚本不做图像理解'),generation_validation='pending',scope='两段格式与已知关系编译，不代表视频空间一致性成功')
    (out/'空间锁编译回执.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    return text

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--scene',required=True);p.add_argument('--out',required=True);a=p.parse_args()
    print(compile_scene(json.loads(Path(a.scene).read_text(encoding='utf-8-sig')),a.out))
