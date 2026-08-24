import json
from datetime import datetime

# 파일 읽기
def load_prompts():
    try:
        with open('prompts.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data ['prompts']
    except FileNotFoundError:
        return []

# 프롬프트 추가
def add_prompt():

    title = input("제목: ")
    content = input("내용: ")
    
    print("\n카테고리를 선택하세요:")
    print("  1. 텍스트 생성")
    print("  2. 이미지 생성")
    print("  3. 영상 생성")
    print("  4. 페르소나")
    print("  5. 자동화")
    print("  6. 기타")
    
    categories = {
        '1': '텍스트 생성',
        '2': '이미지 생성',
        '3': '영상 생성',
        '4': '페르소나',
        '5': '자동화',
        '6': '기타'
    }
    
    while True:
        choice = input("선택 (1-6): ")
        if choice in categories:
            category = categories[choice]
            break
        else:
            print("❌ 1~6 사이의 숫자를 입력하세요!")
    
    while True:
        fav_input = input("즐겨찾기에 추가할까요? (y/n): ").lower()
        if fav_input == 'y':
            favorite = True
            break
        elif fav_input == 'n':
            favorite = False
            break
        else:
            print("❌ y 또는 n만 입력하세요!")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_prompt = {
        "id": len(prompts) + 1,
        "title": title,
        "content": content,
        "category": category,
        "favorite": favorite,
        "created_date": now,  
    }
    
    prompts.append(new_prompt)
    print(f"✅ '{title}' 추가 완료!")

# 프롬프트 조회
def view_prompts():
    """모든 프롬프트 조회"""
    
    if not prompts:
        print("📭 저장된 프롬프트가 없습니다.")
        return
    
    print("\n" + "="*50)
    print("📋 프롬프트 목록")
    print("="*50)
    
    for prompt in prompts:
        print("\n" + "="*50)
        print(f"ID: {prompt['id']}")
        print(f"제목: {prompt['title']}")
        print(f"내용: {prompt['content']}")
        print(f"카테고리: {prompt['category']}")
        print(f"즐겨찾기: {'⭐ 예' if prompt['favorite'] else '아니오'}")
        print(f"생성일: {prompt.get('created_date', '정보 없음')}")  # ✅ .get() 사용!
        print("="*50)
    
    print("\n" + "="*50)

# 프롬프트 삭제
def delete_prompt(prompt_id):
    """프롬프트 삭제"""
    global prompts
    
    # ID로 프롬프트 찾기
    for i, prompt in enumerate(prompts):
        if prompt['id'] == prompt_id:
            prompts.pop(i)
            print(f"✅ ID {prompt_id} 프롬프트가 삭제되었습니다.")
            return
    
    print(f"❌ ID {prompt_id}를 찾을 수 없습니다.")

# 프롬프트 수정
def update_prompt(prompt_id, title, content):
    global prompts
    
    for prompt in prompts:
        if prompt['id'] == prompt_id:
            prompt['title'] = title
            prompt['content'] = content
            print(f"✅ ID {prompt_id} 프롬프트가 수정되었습니다.")
            return
    
    print(f"❌ ID {prompt_id}를 찾을 수 없습니다.")

# 프롬프트 검색
def search_prompt():
    while True:  # 반복해서 검색 가능
        keyword = input("\n검색할 키워드 (종료: q): ")
        
        # 종료 조건
        if keyword.lower() == 'q':
            print("검색을 종료합니다.")
            break
        
        # 빈 입력 처리
        if keyword.strip() == "":
            print("⚠️ 검색어를 입력해주세요!")
            continue
        
        # 검색 실행
        results = []
        for prompt in prompts:
            if keyword in prompt['title'] or keyword in prompt['content']:
                results.append(prompt)
        
 # 결과 없음
        if len(results) == 0:
            print(f"❌ '{keyword}'에 대한 검색 결과가 없습니다.")
            print("다시 검색해주세요!")
            continue
        
        # 결과 목록 출력
        print(f"\n✅ 검색 결과: {len(results)}개")
        print("-" * 40)
        for idx, prompt in enumerate(results, 1):
            print(f"  {idx}. [{prompt['id']}] {prompt['title']}")
        print("-" * 40)
        
        # 상세보기 선택
        while True:
            choice = input("\n상세보기할 번호 선택 (취소: 0): ")
            
            # 취소
            if choice == '0':
                break
            
            # 숫자 검증
            if not choice.isdigit():
                print("⚠️ 숫자를 입력해주세요!")
                continue
            
            choice = int(choice)
            
            # 범위 검증
            if choice < 1 or choice > len(results):
                print(f"⚠️ 1~{len(results)} 사이 번호를 입력해주세요!")
                continue
            
            # 상세 정보 출력
            selected = results[choice - 1]
            print("\n" + "=" * 40)
            print(f"📌 제목: {selected['title']}")
            print(f"🆔 ID: {selected['id']}")
            print("-" * 40)
            print(f"📄 내용:\n{selected['content']}")
            print("=" * 40)
        
        break  # 검색 종료

# 프롬프트 관리 프로그램
prompts  = load_prompts()

def show_menu():
    print("\n=== 프롬프트 관리자 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 조회")
    print("3. 프롬프트 삭제")
    print("4. 프롬프트 수정")
    print("5. 프롬프트 검색")
    print("6. 종료")
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
            add_prompt()
        
        elif choice == "2":
            view_prompts()
        
        elif choice == "3":
            prompt_id = int(input("삭제할 프롬프트 ID: "))
            delete_prompt(prompt_id)
        
        elif choice == "4":
            prompt_id = int(input("수정할 프롬프트 ID: "))
            title = input("새 제목: ")
            content = input("새 내용: ")
            update_prompt(prompt_id, title, content)

        elif choice == "5":
            search_prompt()
        
        elif choice == "6":
            print("종료합니다!")
            break
        
        else:
            print("❌ 잘못된 선택입니다!")

if __name__ == "__main__":
    main()
