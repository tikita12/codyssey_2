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
    # 제목 입력 (빈 값 검증)
    while True:
        title = input("제목: ").strip()
        if title == "":
            print("❌ 제목을 입력해주세요!")
            continue
        break
    
    # 내용 입력 (빈 값 검증)
    while True:
        content = input("내용: ").strip()
        if content == "":
            print("❌ 내용을 입력해주세요!")
            continue
        break
    
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
    
    # ✅ 즐겨찾기 부분 삭제됨!
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_prompt = {
        "id": len(prompts) + 1,
        "title": title,
        "content": content,
        "category": category,
        "created_date": now,  # ✅ favorite 삭제됨!
        "views": 0
    }
    
    prompts.append(new_prompt)
    print(f"✅ '{title}' 추가 완료!")

# 프롬프트 조회
def view_prompts():
    """프롬프트 전체 조회 (제목, 카테고리, 즐겨찾기만)"""
    # 프롬프트가 없으면 안내 메시지
    if not prompts:
        print("\n📭 저장된 프롬프트가 없습니다.")
        return
    
    print("\n📋 프롬프트 목록")
    print("="*40)
    
    for prompt in prompts:
        # 즐겨찾기 표시 (⭐ 또는 ☆)
        star = "⭐" if prompt.get('favorite', False) else "☆"
        
        # 제목 | 카테고리 | 즐겨찾기만 표시
        print(f"ID: {prompt['id']} | {prompt['title']} | {prompt['category']} | {star}")
        
# 즐겨찾기 기능
def toggle_favorite(prompt_id):
    """즐겨찾기 등록/해제 선택"""
    for prompt in prompts:
        if prompt['id'] == prompt_id:
            # 현재 상태 보여주기
            current = prompt.get('favorite', False)
            status = "⭐ 등록됨" if current else "☆ 해제됨"
            print(f"\n현재 상태: {status}")
            
            # 사용자 선택
            print("1. 즐겨찾기 등록")
            print("2. 즐겨찾기 해제")
            choice = input("선택: ")
            
            if choice == '1':
                prompt['favorite'] = True
                print(f"⭐ ID {prompt_id}를 즐겨찾기에 추가했습니다!")
            elif choice == '2':
                prompt['favorite'] = False
                print(f"☆ ID {prompt_id}를 즐겨찾기에서 제거했습니다!")
            else:
                print("❌ 잘못된 선택입니다.")
            return
    
    print(f"❌ ID {prompt_id}를 찾을 수 없습니다.")

# 즐겨찾기 모아보기
def view_favorites():
    """즐겨찾기만 조회"""
    # 즐겨찾기된 것만 필터링
    favorites = [p for p in prompts if p.get('favorite', False)]
    
    if not favorites:
        print("⭐ 즐겨찾기한 프롬프트가 없습니다.")
        return
    
    print("\n" + "="*50)
    print("⭐ 즐겨찾기 목록")
    print("="*50)
    
    for prompt in favorites:
        print(f"\n[{prompt['id']}] {prompt['title']}")
        print(f"  카테고리: {prompt.get('category', '없음')}")
    
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
def update_prompt():   # ← 괄호 비우기!
    """프롬프트 수정"""
    
    if not prompts:
        print("\n📭 저장된 프롬프트가 없습니다.")
        return
    
    # 목록 보여주기
    print("\n📋 프롬프트 목록")
    for prompt in prompts:
        print(f"ID: {prompt['id']} | {prompt['title']}")
    
    # 1. 수정할 ID 입력받기
    num = input("\n수정할 ID: ")
    if not num.isdigit():
        print("❌ 숫자를 입력하세요!")
        return
    
    prompt_id = int(num)
    
    # 2. ID로 찾기
    for prompt in prompts:
        if prompt['id'] == prompt_id:
            
            # 3. 새 값 입력받기
            print(f"\n현재 제목: {prompt['title']}")
            new_title = input("새 제목 (Enter=유지): ")
            
            print(f"현재 내용: {prompt['content']}")
            new_content = input("새 내용 (Enter=유지): ")
            
            # 4. 값 수정 (Enter만 누르면 기존 값 유지!)
            if new_title:
                prompt['title'] = new_title
            if new_content:
                prompt['content'] = new_content
            
            print("✅ 수정 완료!")
            return
    
    print(f"❌ ID {prompt_id}번을 찾을 수 없습니다!")

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
        
        # 상세보기 선택
        while True:
            choice = input("\n상세보기할 번호 선택 (취소: 0): ")
            
            if choice == '0':  # 취소
                break
            
            if choice.isdigit() and 1 <= int(choice) <= len(results):
                prompt = results[int(choice) - 1]
                
                prompt['views'] += 1  # ← 조회수 증가! 📈 (핵심!)
                
                # 상세 정보 출력
                print("\n" + "="*40)
                print(f"제목: {prompt['title']}")
                print(f"카테고리: {prompt['category']}")
                print(f"내용: {prompt['content']}")
                print(f"작성일: {prompt['created_date']}")
                print(f"👁️ 조회수: {prompt['views']}")  # 조회수 표시!
                print("="*40)
            else:
                print("❌ 올바른 번호를 입력하세요!")
        
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

#카테고리 보기
def view_by_category():
    """카테고리별 조회"""
    if not prompts:
        print("📭 저장된 프롬프트가 없습니다.")
        return
    
    # 1. 존재하는 카테고리 목록 만들기 (중복 제거)
    categories = set()
    for prompt in prompts:
        categories.add(prompt['category'])
    
    categories = sorted(categories)  # 정렬
    
    # 2. 카테고리 목록 보여주기
    print("\n📂 카테고리 목록")
    print("="*40)
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    # 3. 사용자 선택
    choice = input("\n조회할 카테고리 번호: ")
    
    # 4. 입력 검증
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(categories):
        print("❌ 잘못된 번호입니다.")
        return
    
    # 5. 선택한 카테고리
    selected = categories[int(choice) - 1]
    
    # 6. 해당 카테고리 프롬프트 출력
    print(f"\n📋 '{selected}' 카테고리 프롬프트")
    print("="*40)
    
    for prompt in prompts:
        if prompt['category'] == selected:
            star = " (⭐)" if prompt.get('favorite', False) else ""
            print(f"ID: {prompt['id']}, 제목: {prompt['title']}{star}")

# 프롬프트 상세내용 보기
def view_prompt_detail():
    """목록 보여주고 → 번호 선택 → 상세 정보 출력"""
    
    # 프롬프트 없으면 종료
    if not prompts:
        print("\n📭 저장된 프롬프트가 없습니다.")
        return
    
    # 1단계: 목록 먼저 보여주기
    print("\n📋 프롬프트 목록")
    print("="*40)
    for prompt in prompts:
        star = "⭐" if prompt.get('favorite', False) else "☆"
        print(f"ID: {prompt['id']} | {prompt['title']} | {prompt['category']} | {star}")
    print("="*40)
    
    # 2단계: 번호 입력받기
    num = input("\n상세히 볼 ID: ")
    
    # 숫자인지 확인 (잘못된 입력 처리)
    if not num.isdigit():
        print("❌ 숫자를 입력해주세요!")
        return
    
    prompt_id = int(num)
    
    # 3단계: ID로 프롬프트 찾기
    for prompt in prompts:
        if prompt['id'] == prompt_id:
            
            prompt['views'] += 1  # 📈 조회수 증가! (핵심!)
            
            # 즐겨찾기 표시
            star = "⭐ 등록됨" if prompt.get('favorite', False) else "☆ 해제됨"
            
            # 4단계: 상세 정보 출력
            print("\n" + "="*40)
            print(f"📌 제목: {prompt['title']}")
            print(f"📁 카테고리: {prompt['category']}")
            print(f"⭐ 즐겨찾기: {star}")
            print(f"👁️ 조회수: {prompt['views']}")
            print("-"*40)
            print(f"📝 내용:\n{prompt['content']}")
            print("="*40)
            return  # 찾았으니 함수 종료
    
    # 못 찾았을 때 (잘못된 번호)
    print(f"❌ ID {prompt_id}번 프롬프트를 찾을 수 없습니다!")

#조회수 순위
def view_top_prompts():
    """조회수 Top 순위 보기"""
    if not prompts:
        print("\n📭 프롬프트가 없습니다.")
        return
    
    # 조회수 높은 순으로 정렬! ⭐
    sorted_prompts = sorted(prompts, key=lambda x: x['views'], reverse=True)
    
    print("\n" + "="*40)
    print("🏆 인기 프롬프트 TOP")
    print("="*40)
    
    for i, prompt in enumerate(sorted_prompts, 1):
        # 순위별 메달 이모지 🥇🥈🥉
        if i == 1:
            medal = "🥇"
        elif i == 2:
            medal = "🥈"
        elif i == 3:
            medal = "🥉"
        else:
            medal = f"{i}위"
        
        print(f"{medal} {prompt['title']} (👁️ {prompt['views']}회)")
    print("="*40)

# 프롬프트 관리 프로그램
prompts  = load_prompts()

def show_menu():
    print("\n=== 프롬프트 관리자 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 프롬프트 삭제")
    print("4. 프롬프트 수정")
    print("5. 프롬프트 검색")
    print("6. 즐겨찾기 등록/해제")  
    print("7. ⭐ 즐겨찾기만 보기") 
    print("8. 카테고리별 조회")
    print("9. 상세내용 조회")
    print("10. 인기 순위")
    print("0. 종료")
    choice = input("선택: ")
    return choice

def show_list():
    print("\n=== 프롬프트 목록 ===")
    for p in prompts:
        print(f"{p['id']}. {p['title']}")

def main():
    while True:
        choice = show_menu()
        
        if choice == '1':
            add_prompt()
        elif choice == '2':
            view_prompts()
        elif choice == '3':
            delete_prompt()
        elif choice == '4':
            update_prompt()
        elif choice == '5':
            search_prompt()
        elif choice == '6':
            view_prompts()
            prompt_id = int(input("즐겨찾기 토글할 ID: "))
            toggle_favorite(prompt_id)
        elif choice == '7':
            view_favorites()
        elif choice == '8':
            view_by_category()
        elif choice == '9':
            view_prompt_detail()
        elif choice == '10':
            view_top_prompts()
        elif choice == "0":
            print("종료합니다!")
            break
        
        else:
            print("❌ 잘못된 선택입니다!")

if __name__ == "__main__":
    main()
