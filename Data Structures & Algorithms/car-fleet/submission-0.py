class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(key=lambda x: x[0])
        
        stack = []
        for car in cars:
            while stack and self.time(target, stack[-1][0], stack[-1][1]) <= self.time(target, car[0], car[1]):
                stack.pop()
            stack.append(car)

        return len(stack)

    def time(self, target, pos, speed):
        return (target - pos) / speed