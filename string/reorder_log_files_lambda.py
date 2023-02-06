def reorderLogFiles(self, logs: list[str]) -> list[str]:
  letters, digits = [], []
  for log in logs:
    if log.split()[1].isdigit():
      digits.append(log)
    else:
      letters.append(log)

  # sort with lambda
  # 문자가 동일할 경우에만 식별자 순으로 정렬
  # [1:] 식별자를 제외한 문자열을 키로 하여 정렬
  # 문자가 동일하면, 후순위로 식별자를 키로 정렬
  letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
  return letters + digits

