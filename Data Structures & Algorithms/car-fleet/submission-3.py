class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_sp_map={}
        stack=[]
        for i in range (len(position)):
            pos_sp_map[position[i]]=speed[i]
        position = sorted(position,reverse = True)
        fleet = len(position)
        for i in range(len(position)):

            cur_speed=pos_sp_map[position[i]]
            time = (target-position[i])/cur_speed
            if len(stack)>0:
                if time>stack[-1]:
                    stack.append(time)

            if i == 0:
                stack.append(time)

           
        
         
        return len(stack)