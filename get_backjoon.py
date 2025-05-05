import requests
from bs4 import BeautifulSoup
import json
import re
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
import os

def get_problem_info(problem_number):
    problem_url = f"https://www.acmicpc.net/problem/{problem_number}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(problem_url, headers=headers)
        response.raise_for_status()  # 오류 발생시 예외 발생
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 문제 제목 가져오기
        title = soup.select_one('#problem_title').text.strip()
        
        # 문제 설명 가져오기
        description = soup.select_one('#problem_description').text.strip()
        
        # 입력 설명 가져오기
        input_description = soup.select_one('#problem_input').text.strip()
        
        # 출력 설명 가져오기
        output_description = soup.select_one('#problem_output').text.strip()
        
        # 예제 입력 가져오기
        sample_inputs = []
        sample_outputs = []
        
        for i, sample_input in enumerate(soup.select('.sampledata[id^=sample-input]')):
            sample_inputs.append(sample_input.text.strip())
            
        for i, sample_output in enumerate(soup.select('.sampledata[id^=sample-output]')):
            sample_outputs.append(sample_output.text.strip())
        
        difficulty = get_difficulty(problem_number)
        algorithm_type = get_algorithm_type(problem_number)
        
        return {
            'problem_number': problem_number,
            'title': title,
            'description': description,
            'input_description': input_description,
            'output_description': output_description,
            'sample_inputs': sample_inputs,
            'sample_outputs': sample_outputs,
            'difficulty': difficulty,
            'algorithm_type': algorithm_type,
            'problem_url': problem_url
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching problem: {e}")
        return None

def get_difficulty(problem_number):
    try:
        url = f"https://solved.ac/api/v3/problem/show?problemId={problem_number}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        level = data.get('level', 0)
        
        # solved.ac 레벨을 난이도로 변환
        tiers = {
            1: "Bronze 5", 2: "Bronze 4", 3: "Bronze 3", 4: "Bronze 2", 5: "Bronze 1",
            6: "Silver 5", 7: "Silver 4", 8: "Silver 3", 9: "Silver 2", 10: "Silver 1",
            11: "Gold 5", 12: "Gold 4", 13: "Gold 3", 14: "Gold 2", 15: "Gold 1",
            16: "Platinum 5", 17: "Platinum 4", 18: "Platinum 3", 19: "Platinum 2", 20: "Platinum 1",
            21: "Diamond 5", 22: "Diamond 4", 23: "Diamond 3", 24: "Diamond 2", 25: "Diamond 1",
            26: "Ruby 5", 27: "Ruby 4", 28: "Ruby 3", 29: "Ruby 2", 30: "Ruby 1",
        }
        
        return tiers.get(level, "Unknown")
        
    except Exception as e:
        print(f"Error fetching difficulty: {e}")
        return "Unknown"

def get_algorithm_type(problem_number):
    try:
        url = f"https://solved.ac/api/v3/problem/show?problemId={problem_number}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        tags = data.get('tags', [])
        
        algorithm_types = []
        for tag in tags:
            if 'displayNames' in tag and tag['displayNames']:
                for display_name in tag['displayNames']:
                    if display_name['language'] == 'ko':
                        algorithm_types.append(display_name['name'])
                        break
        
        return algorithm_types if algorithm_types else ["Not specified"]
        
    except Exception as e:
        print(f"Error fetching algorithm type: {e}")
        return ["Unknown"]

def create_notebook(problem_info):
    nb = new_notebook()
    
    # 문제 정보 마크다운 셀
    problem_info_md = f"""# 📝 문제 정보 (BOJ {problem_info['problem_number']})
* 문제 이름: {problem_info['title']}
* 문제 링크: {problem_info['problem_url']}
* 난이도: {problem_info['difficulty']}
* 알고리즘 유형: {', '.join(problem_info['algorithm_type']) if isinstance(problem_info['algorithm_type'], list) else problem_info['algorithm_type']}

## 문제 설명
{problem_info['description']}

### 입력
{problem_info['input_description']}

### 출력
{problem_info['output_description']}

### 예제 입력 1
```
입력:
{problem_info['sample_inputs'][0] if problem_info['sample_inputs'] else ''}
출력:
{problem_info['sample_outputs'][0] if problem_info['sample_outputs'] else ''}
```
"""
    
    # 추가 예제가 있는 경우
    for i in range(1, min(len(problem_info['sample_inputs']), len(problem_info['sample_outputs']))):
        problem_info_md += f"""
### 예제 입출력 {i+1}
```
입력:
{problem_info['sample_inputs'][i]}
출력:
{problem_info['sample_outputs'][i]}
```
"""
    
    nb.cells.append(new_markdown_cell(problem_info_md))
    
    # 접근 방법 마크다운 셀
    approach_md = """# 💡 접근 방법
1. 
2. 
3. 

# ⏱️ 시간복잡도
O()

# 🗃️ 공간복잡도
O()
"""
    nb.cells.append(new_markdown_cell(approach_md))
    
    # 코드 셀
    code = """# 코드 작성
def solution():
    # 여기에 코드를 작성하세요
    pass

# 입력 처리
if __name__ == "__main__":
    solution()
"""
    nb.cells.append(new_code_cell(code))
    # 배운 점 & 어려웠던 점 마크다운 셀
    learned_md = """# 🧐 배운 점 & 어려웠던 점
- 
- 
- 

# ✅ 자가 체크리스트
- [ ] 코드가 모든 테스트 케이스를 통과하나요?
- [ ] 더 최적화할 수 있는 방법이 있나요?
- [ ] 코드에 주석을 충분히 달았나요?
"""
    nb.cells.append(new_markdown_cell(learned_md))
    
    return nb

def save_notebook(notebook, problem_number, title, algorithm_type):
    # 파일명에 사용할 수 없는 문자 제거
    safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
    file_name = f"BOJ_{problem_number}_{safe_title}.ipynb"
    
    # 알고리즘 유형으로 저장 디렉토리 설정
    if isinstance(algorithm_type, list) and algorithm_type:
        # 리스트인 경우 첫 번째 알고리즘 유형을 디렉토리 이름으로 사용
        save_dir = re.sub(r'[\\/*?:"<>|]', "", algorithm_type[0])
    else:
        # 문자열이거나 빈 리스트인 경우 그대로 사용
        save_dir = re.sub(r'[\\/*?:"<>|]', "", algorithm_type if isinstance(algorithm_type, str) else "기타")
    
    # 디렉토리가 없으면 생성
    os.makedirs(save_dir, exist_ok=True)
    
    file_path = os.path.join(save_dir, file_name)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)
    
    return file_path

def main():
    try:
        problem_number = int(input("백준 문제 번호를 입력하세요: "))
        
        print(f"백준 {problem_number}번 문제 정보를 가져오는 중...")
        problem_info = get_problem_info(problem_number)
        
        if problem_info:
            print(f"문제: {problem_info['title']}")
            print(f"난이도: {problem_info['difficulty']}")
            print(f"알고리즘 유형: {', '.join(problem_info['algorithm_type']) if isinstance(problem_info['algorithm_type'], list) else problem_info['algorithm_type']}")
            
            print("\nJupyter Notebook 파일 생성 중...")
            notebook = create_notebook(problem_info)
            
            file_path = save_notebook(notebook, problem_number, problem_info['title'], problem_info['algorithm_type'])
            print(f"\n파일이 성공적으로 저장되었습니다: {file_path}")
        else:
            print("문제 정보를 가져오는데 실패했습니다.")
    
    except ValueError:
        print("올바른 문제 번호를 입력해주세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()