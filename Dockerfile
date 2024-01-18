# For more information, please refer to https://aka.ms/vscode-docker-python
FROM centos:7

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
RUN yum install python3 python-psutil pyyaml git -y

RUN git clone https://github.com/tpratyushareddy/rescaling.git /tmp/rescaling
WORKDIR /tmp/rescaling

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3", "cpu_usage_display.py"]
