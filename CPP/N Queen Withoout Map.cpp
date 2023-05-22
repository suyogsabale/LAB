#include <iostream>
#include <vector>
#include <algorithm>
#include<map>
using namespace std;

bool isSafe(int row,int col,vector<vector<char>>& board,int n)
{
  //rowcheck
  int i=row;
  int j=col;
  while(j>=0)
    {
      if(board[i][j]=='Q')
         return false;
      j--;
    }
//left upper
  i=row;
  j=col;
  while(i>=0&&j>=0)
    {
      if(board[i][j]=='Q')
        return false;
      i--;
      j--;
    }

  i=row;
  j=col;
  while(i<n&&j>=0)
    {
      if(board[i][j]=='Q')
        return false;
      i++;
      j--;
    }
  return true;
}
 void  print(vector<vector<char>>& board,int n)
{
  for(int i=0;i<n;i++)
    {
      for(int j=0;j<n;j++)
        {
          cout<<board[i][j];
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
  //recursion start
  for(int row=0;row<n;row++)
    {
      if(isSafe(row,col,board,n))
       { board[row][col]='Q';

      //recursion call
    solve( n,  board, col+1);
      //backtracking
        board[row][col]='.';}
    }
}

int main() {
  int n=4;
   vector<vector<char>> board(n,vector<char>(n,'.'));
  int col=0;
  solve(n,board,col);
  
 return 0;
}


