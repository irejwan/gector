import re
from setuptools import setup, find_packages

try:
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements


_egg_fragment_re = re.compile(r'[#&]egg=([^&]*)')


def req(ir):
    res = getattr(ir, 'req', None)
    if res is None:
        res = getattr(ir, 'requirement', None)
    assert res is not None, f'Could not infer requirement: {ir}'
    res = str(res)
    link = getattr(ir, 'link', None)
    if link is not None:
        res = f'{res} @ {link.url}'
    elif '://' in res:
        m = _egg_fragment_re.search(res)
        assert m, f'Please provide #egg=<package_name> for requirement: {res}'
        package_name = m.group(1)
        res = f'{package_name} @ {res}'
    return res


setup(name='gector',
      version='1.00_master',
      description="GECToR – Grammatical Error Correction: Tag, Not Rewrite",
      url='https://github.com/irejwan/gector.git',
      author='irejwan',
      install_requires=[req(ir) for ir in parse_requirements('requirements.in', session=True)],
      packages=find_packages(exclude=("test", "test.*", "test_system", "test_system.*")),
      zip_safe=False,
      package_data={})
