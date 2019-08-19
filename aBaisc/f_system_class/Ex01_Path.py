"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path


# (1) 해당 경로와 하위 목록들 확인


# (2) 파일시스템에 해당 파일이 존재하는지 여부


# (3) 윈도우는 경로 구분자로 역슬래쉬를 사용하지만 Path를 사용하면 슬래쉬로도 인식하여
# 운영체제의 영향없이 추상화하여 path를 사용할 수 있다

