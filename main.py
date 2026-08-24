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
def add_prompt(title, content):
    global prompt
    
    # 새 ID 만들기 (가장 큰 ID + 1)
    new_id = max([p['id'] for p in prompts], default=0) + 1
    
    # 새 프롬프트 만들기
    new_prompt = {
        "id": new_id,
        "title": title,
        "content": content,
        "created_date": datetime.now().strftime("%Y-%m-%d")
    }
    
    # 추가
    prompts.append(new_prompt)
    print(f"✅ 프롬프트 추가 완료! (ID: {new_id})")

# 프롬프트 조회
def view_prompts():
    """모든 프롬프트 조회"""
    global prompt
    
    if not prompts:
        print("📭 저장된 프롬프트가 없습니다.")
        return
    
    print("\n" + "="*50)
    print("📋 프롬프트 목록")
    print("="*50)
    
    for prompt in prompts:
        print(f"\n[ID: {prompt['id']}] {prompt['title']}")
        print(f"내용: {prompt['content']}")
        print(f"생성일: {prompt['created_date']}")
    
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
            title = input("제목: ")
            content = input("내용: ")
            add_prompt(title, content)
        
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
