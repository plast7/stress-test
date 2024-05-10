import subprocess

def compile_cpp(source_file, output_file):
    subprocess.run(["g++", "-std=c++17", "-o", output_file, source_file], check=True)

def run_program(program, input_data):
    result = subprocess.run(program, input=input_data, text=True, capture_output=True)
    return result.stdout

def generate_input_from_py():
    # 'gen.py' 스크립트 실행
    result = subprocess.run(["python3", "gen.py"], capture_output=True, text=True)
    return result.stdout

def main():
    source1 = 'program1.cpp'
    source2 = 'program2.cpp'
    exe1 = './program1'
    exe2 = './program2'

    # C++ 프로그램 컴파일
    compile_cpp(source1, exe1)
    compile_cpp(source2, exe2)

    while True:
        input_data = generate_input_from_py()

        # 프로그램 실행
        output1 = run_program([exe1], input_data)
        output2 = run_program([exe2], input_data)

        # 출력 비교
        if output1 != output2:
            print(f"다른 출력 발견! 입력\n{input_data.strip()}\n\n@@ 출력1\n{output1.strip()}\n\n@@ 출력2\n{output2.strip()}")
            break
        else:
            print(f"동일한 출력")

if __name__ == "__main__":
    main()
