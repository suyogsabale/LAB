#include <iostream>
#include <vector>
#include <algorithm>
#include<unordered_map>
using namespace std;

unordered_map<int,bool> rowCheck;
unordered_map<int,bool> upperCheck;
unordered_map<int,bool> lowerCheck;



bool isSafe(int row,int col,vector<vector<char>>& board,int n)
{
  //rowcheck
 if(rowCheck[row]==true)
   return false;
 
//left upper
 if(upperCheck[n-1+col-row]==true)
   return false;
 
 //left lower
 if(lowerCheck[row+col]==true)
   return false;

  
  return true;
}
 void  print(vector<vector<char>>& board,int n)
{
  for(int i=0;i<n;i++)
    {
      for(int j=0;j<n;j++)
        {
          cout<<board[i][j]<<" ";
        }cout<<endl;
    }
  cout<<endl;

}
void solve(int n, vector<vector<char>>& board,int col)
{
  //base case
  if(col>=n)
  {
    print(board,n);
    return;
  }
  //recursion
  for(int row=0;row<n;row++)
    {
      if(isSafe(row,col,board,n))
       { board[row][col]='Q';
         rowCheck[row]=true;
         upperCheck[n-1+col-row]=true;
         lowerCheck[row+col]=true;

      //recursion ch kam
    solve( n,  board, col+1);
      //backtracking
        board[row][col]='-';
        rowCheck[row]=false;
         upperCheck[n-1+col-row]=false;
         lowerCheck[row+col]=false;
       }
    }
}

int main() {
  int n;
  cout<<"\nEnter the number of Queens:-";
  cin>>n;
   vector<vector<char>> board(n,vector<char>(n,'-'));
  int col=0;
  solve(n,board,col);
  
 return 0;
}




