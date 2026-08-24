# 프롬프트 관리 프로그램
prompts = [
    {"id": 1, "title": "ChatGPT 글쓰기", "content": "전문적인 이메일을 작성해줘"},
    {"id": 2, "title": "코딩 도움", "content": "Python 함수 설명해줘"},
    {"id": 3, "title": "아이디어 생성", "content": "마케팅 아이디어 10개 줘"}
]

def show_menu():
    print("\n=== 프롬프트 관리자 ===")
    print("1. 프롬프트 목록 보기")
    print("2. 프롬프트 추가")
    print("3. 프롬프트 삭제")
    print("4. 종료")
    choice = input("선택: ")
    return choice

def show_list():
    print("\n=== 프롬프트 목록 ===")
    for p in prompts:
        print(f"{p['id']}. {p['title']}")

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            show_list()
        elif choice == "4":
            print("종료합니다!")
            break
        else:
            print("잘못된 선택입니다")

if __name__ == "__main__":
    main()
    