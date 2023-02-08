# 42
def trap(self, height: list[int]) -> int:
  stack = []
  volume = 0

  for i in range(len(height)):
    # facing inflection point
    while stack and height[i] > height[stack[-1]]:
      top = stack.pop()

      if not len(stack):
        break
      # current - previous inflection point - 1
      distance = i - stack[-1] - 1
      waters = min(height[i], height[stack[-1]]) - height[top]

      volume += distance * waters
    # append inflection point i
    stack.append(i)
  return volume