import argparse
import subprocess
import os

def prepare_program(source_file):
    """
    파일 확장자에 따라 컴파일 혹은 실행 명령어를 준비합니다.
    
    - C++ (.cpp): g++로 컴파일 후, 실행 파일 경로를 반환
    - Java (.java): javac로 컴파일 후, "java [클래스명]" 명령어 리스트 반환
    - Python (.py): 바로 "python3 [파일명]" 명령어 리스트 반환
    """
    ext = os.path.splitext(source_file)[1]
    if ext == ".cpp":
        # C++ 소스 파일 컴파일
        exe = "./" + os.path.splitext(os.path.basename(source_file))[0]
        print(f"C++ 파일 컴파일 중: {source_file} -> {exe}")
        subprocess.run(["g++", "-std=c++17", "-o", exe, source_file], check=True)
        return [exe]
    elif ext == ".java":
        # Java 소스 파일 컴파일
        print(f"Java 파일 컴파일 중: {source_file}")
        subprocess.run(["javac", source_file], check=True)
        classname = os.path.splitext(os.path.basename(source_file))[0]
        return ["java", classname]
    elif ext == ".py":
        # Python은 컴파일 없이 바로 실행
        return ["python3", source_file]
    else:
        raise ValueError(f"지원하지 않는 파일 확장자: {ext}")

def run_program(program, input_data):
    """
    지정된 프로그램을 실행하고, 표준 입력으로 input_data를 전달한 뒤,
    표준 출력을 문자열로 반환합니다.
    """
    result = subprocess.run(program, input=input_data, text=True, capture_output=True)
    return result.stdout

def generate_input():
    """
    'gen.py' 스크립트를 실행하여 테스트 입력 데이터를 생성합니다.
    """
    result = subprocess.run(["python3", "gen.py"], capture_output=True, text=True)
    return result.stdout

def main():
    parser = argparse.ArgumentParser(description="두 프로그램의 출력을 비교하는 스트레스 테스트")
    parser.add_argument("prog1", help="첫 번째 프로그램 소스 파일 (C++/Java/Python)")
    parser.add_argument("prog2", help="두 번째 프로그램 소스 파일 (C++/Java/Python)")
    args = parser.parse_args()

    try:
        cmd1 = prepare_program(args.prog1)
        cmd2 = prepare_program(args.prog2)
    except subprocess.CalledProcessError as e:
        print(f"컴파일 오류: {e}")
        return
    except ValueError as e:
        print(e)
        return

    iteration = 0
    while True:
        iteration += 1
        input_data = generate_input()

        output1 = run_program(cmd1, input_data)
        output2 = run_program(cmd2, input_data)

        if output1 != output2:
            print(f"[{iteration}] 다른 출력 발견!")
            print(f"입력:\n{input_data.strip()}")
            print(f"\n@@ 출력1:\n{output1.strip()}")
            print(f"\n@@ 출력2:\n{output2.strip()}")
            break
        else:
            print(f"[{iteration}] 동일한 출력")

if __name__ == "__main__":
    main()
