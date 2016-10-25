FROM python:2.7.11-onbuild
RUN pip install pytest
RUN pytest /usr/src/app/test_unit.py
CMD ["python", "-u", "run.py"]
