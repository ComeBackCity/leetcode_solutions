public class Solution {
    public int NumIslands(char[][] grid) {
        int row = grid.Length, col = grid[0].Length;
        bool [,] visited = new bool[row, col];
        
        bool valid(int x, int y){
            if( x < 0 || x >= row || y < 0 || y >= col){
                return false;
            }
            
            return true;
        }
        
        (int x, int y)[] directions = new (int, int)[] {(-1, 0), (1, 0), (0, -1), (0, 1)};
        
        void dfs(int x, int y){
            visited[x, y] = true;
            foreach(var direction in directions){
                int newX = x + direction.x , newY = y + direction.y;
                if(valid(newX, newY) && grid[newX][newY] == '1' && !visited[newX, newY]){
                    dfs(newX, newY);
                }
            }
        }
        
        int islands = 0;
        for (int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(!visited[i, j] && grid[i][j] == '1'){
                    dfs(i, j);
                    islands++;
                }
            }
        }
        
        return islands;
    }
}