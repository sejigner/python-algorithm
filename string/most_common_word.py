#

def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
  words = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split() if word not in banned] # r : raw string 입력한 문자열 그대로 인식
  
  counts = collections.Counter(words)
  # [0][0] [('key', amount)]  key에 접근하기 위해 리스트의 첫번째 튜플의 첫번째 인덱스
  return counts.most_common(1)[0][0]
