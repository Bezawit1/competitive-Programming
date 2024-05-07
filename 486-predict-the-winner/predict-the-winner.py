class Solution(object):
    def predictTheWinner(self, nums):
        """
        state: left pointer , right pointer , turns
        basecase:left >right
        recursive_case:
          if player1 turn 
            get the max of either the left or right
            max_score = max(arr[left] + winner(left + 1 , right , 2), arr[right] + winner(left , right -1 ,2))
            minimize the score for player 2
            track the visited index
        """
        visited = {}
        def winner(left , right , turn):
            if left > right:
                return 0
            if (left , right , turn) in visited:
                return visited[(left , right , turn)]
            ans = 0 
            if turn == 0:
                ans = max(nums[left]+ winner(left +1 , right , 1),nums[right]+ winner(left , right-1  , 1))
            else:
                ans = min( winner(left +1 , right , 0), winner(left , right -1  , 0))
            visited[(left , right,turn)] = ans
            return ans
        player1_score = winner(0,len(nums)-1 , 0)
        player2_score = sum(nums) - player1_score
        return player2_score <=player1_score








        
        