import re

# text全局参数替换
def global_replace(text, comp, transform=False):
    if transform:
        comp = {"{%s}" % k: v for k, v in comp.items() if isinstance(v, str)}
    text = re.sub(f'({"|".join(comp.keys())})', lambda x: comp.get(x.group(1), x.group(1)), text)
    return text
