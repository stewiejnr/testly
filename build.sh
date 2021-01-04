rm -rf dist/*
python setup.py sdist bdist_wheel
pip uninstall -y testly
FILEN=$(basename dist/*.whl)
pip install dist/$FILEN -I