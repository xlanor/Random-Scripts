
**Preamble**

**Colloboration Policy**. The student is to *explicitly identify* his/her collaborators in the assignment. If the student did not work with anyone, he/she should indicate `Collaborators=['none']`. If the student obtains a solution through research (e.g., on the web), acknowledge the source, but write up the solution in his/her own words. There will be a one mark penalty if a student fails to indicate his/her collaborators.

**Submission Deadline**. I will allow late submissions. However, a late submission will be subject to a penalty that is commensurate to the 'lateness'. Specifically, the penalty is as follows.
```
* Before 18 Apr (Wed), 13:00hrs                    = No penalty
* 18 Apr (Wed), 13:01hrs to 22 Mar (Thu), 13:00hrs = 1 Mark Penalty
* 19 Apr (Thu), 13:01hrs to 23 Mar (Fri), 13:00hrs = 2 Marks Penalty
* 20 Apr (Fri), 13:01hrs to 24 Mar (Sat), 13:00hrs = 3 Marks Penalty
* 21 Apr (Sat), 13:01hrs to 25 Mar (Sun), 13:00hrs = 4 Marks Penalty
* 22 Apr (Sun), 13:01hrs to 26 Mar (Mon), 13:00hrs = 5 Marks Penalty
* After 23 Apr (Mon), 13:01hrs                     = Assignment is no longer graded.
```


**There will be NO EXCEPTIONS to this grading policy.**


```python
Name = 'Tan Lerk Tanner'
Collaborators = 'None'


# Indicate your submission time. You may deviate slightly from the actual submission time. Be mindful that I am able to check the edit history.

date = 18 # CHANGETHIS # DATE ONLY. I.E. INTEGER BETWEEN 1 and 30
hour = 12 #'Enter the hour (in 24 hours format)'
date = 18
hour = 12

print('Your name is {}.'.format(Name))
print('Your collaborators are {}.'.format(Collaborators))
print('Your submission is on {} Apr at {}00hrs.'.format(date,hour))
print()

penalty=0
    
penalty += date-18

if (hour>13): penalty+=1    
    
if penalty>=5:
    
    print("******************")
    print("Your assignment is NOT graded.")
    print("******************")

    
else:
    
    penalty=max([0,penalty])
    
    pc=0
    if Collaborators=='' or Collaborators=='CHANGETHIS': 
        penalty+=1
        pc=1
    
    print("******************")
    print("Your penalty: {}".format(penalty))
    if(pc>0): print("You were penalized for not indicating your collaborators!")
    print("******************")
```

    Your name is Tan Lerk Tanner.
    Your collaborators are None.
    Your submission is on 18 Apr at 1200hrs.
    
    ******************
    Your penalty: 0
    ******************


# Assignment 3

## May the odds be ever in your favour

In your school, the class monitor is elected every semester. There are $n$ columns of students in the class seating arrangement, with each column containing $m$ students. Here, $n$ and $m$ are assumed to be even.

As the incumbent monitor, you enjoyed overwhelming support in the previous election. However, due to the massive fight in the class outing, almost half the class now dislikes you. You still have friends on whom you can rely to vote for you, but these friends are distributed across the $n$ columns.

How the election works is that the class will be divided into two halves: left and right. If you have _more than half_ of votes in both halves, then you will be re-elected. As the incumbent, you have the freedom to assign which columns go into which half of the class. How do you maximise your chances?

**Example**. Suppose that $n=4$ and $m=10$. The distribution of your voters are as such:

\begin{array}{|c|cccc|}
\hline
\text{Column} & 1 & 2 & 3 & 4 \\
\hline
\text{Voting for you} & 6 & 4 & 7 & 5 \\
\text{Voting against} & 4 & 6 & 3 & 5 \\\hline 
\end{array}

(In your code, this will be given as a list `votes = [6, 4, 7, 5]`, with $m$ specified as another parameter.)

By default, we assign columns $1$ and $2$ to the left half, and columns $3$ and $4$ to the right half.
However, you only have 10 votes on the left side, which is not sufficient to guarantee the win. 
On the other hand, if we assign columns $1$ and $4$ to the left half, and columns $2$ and $3$ to the right half,
then you will have 11 votes on both halves of the class, securing your re-election.
If we run through all possibilities, we have the following 
(see problem description for definitions of $v_L$ and $v_R$)

\begin{array}{|c|c|c|c|c|}
\hline
\text{left} & \text{right} & v_L & v_R  & \text{outcome} \\
\hline
[1,2] & [3,4] & 10 & 12 & \text{wins right only}\\
[1,3] & [2,4] & 13 & 9 &\text{wins left only}\\
[1,4] & [2,3] & 11 & 11 &\text{wins both!}\\
\hline 
\end{array}


## Problem description

> You are given a class with $n$ columns containing $m$ students per column and information on how many votes you have per column (list `votes`). 
>Determine if it is possible to arrange the columns into two halves such that you have a *majority* in both halves of the class.

Define $v_i$ to be the number of votes for you in column $i$ and $v$ to be the total number of votes for you. 


1. To win in both halfs, we need $$v  \geq \frac{1}{2}mn + 2.$$ 

After arranging the class, define $v_L$ and $v_R$ to be the number of votes for you in the left and right halves respectively. 

2. In order to win the left half, we need $$v_L \geq \frac{1}{4}mn+1.$$ 

3. In order to win the right half, we need that $v_R = v - v_L \geq \frac{1}{4}mn+1$, or $$v_L \leq  v - \frac{1}{4}mn -1.$$

4. To conclude, it is possible to win if there exists a configuration of the class such that $$\frac{1}{4}mn+1 \leq v_L \leq  v - \frac{1}{4}mn -1.$$ 

Returning to our example, $m=10$, $n=4$ and $v=22$. So, $\frac{1}{4}mn+1=11$ and $v-\frac{1}{4}mn-1=11$.
You are able to win because there is an arrangement such that $v_L=11$.

**(a) Identify a suitable collection of subproblems. (2 marks)**

*Your answer goes here*. You can double click this line to edit. $\LaTeX$ is supported within two dollar signs ($). Press Shift+Enter to render.

**(b) Propose and prove a recursion for ${\tt possible }(i,j,k)$. (2 marks)**

*Your answer goes here*. You can double click this line to edit. $\LaTeX$ is supported within two dollar signs ($). Press Shift+Enter to render.

**( c ) Build your solutions. (2 marks)**

(i) Determine ${\tt possible }(i,1,k)$.

*Your answer goes here*. You can double click this line to edit. $\LaTeX$ is supported within two dollar signs ($). Press Shift+Enter to render.

(ii) Determine an order for evaluating ${\tt possible }(i,j,k)$ and explain why it works.

*Your answer goes here*. You can double click this line to edit. $\LaTeX$ is supported within two dollar signs ($). Press Shift+Enter to render.

(iii) Determine the condition that states a winning configuration exists.

*Your answer goes here*. You can double click this line to edit. $\LaTeX$ is supported within two dollar signs ($). Press Shift+Enter to render.

**(d) Evaluate the space and running time. (2 marks)**

(i) Determine the intermediate results that you will be storing.

*Your answer goes here*. You can double click this line to edit. $\LaTeX$ is supported within two dollar signs ($). Press Shift+Enter to render.

(ii) Determine the running time. The running time will be of the form $O(m^r n^s$) for some integers $r,s$.

*Your answer goes here*. You can double click this line to edit. $\LaTeX$ is supported within two dollar signs ($). Press Shift+Enter to render.

**(e) Implement your routine to determine if winning the election is possible. (2 marks)**


```python
def winnable(votes, m):
    n = len(votes)     # Number of columns
    v = sum(votes)

    # your code goes here

    return # CHANGETHIS
```


```python
# Your routine will be tested against the following six vote lists.

votes1 = [5]*28+[6]*2
m1 = 10

votes2 = [5]*29+[10]*1
m2 = 10

votes3 =  [8, 8, 16, 12, 12, 12, 4, 4, 12, 4, 4, 4, 8, 12, 12, 8, 8, 16, 12, 4, 16, 16, 12, 16, 12, 16, 12, 4, 16, 4, 4, 12, 4, 12, 12, 4, 16, 12, 16, 8]
m3 =  20

votes4 =  [22, 21, 34, 39, 28, 33, 32, 40, 22, 34, 36, 27, 37, 34, 40, 38, 39, 32, 37, 40, 31, 37, 22, 21, 35, 34, 24, 40, 34, 21, 24, 20, 30, 31, 22, 30, 31, 25, 20, 38, 24, 23, 32, 27, 20, 31, 27, 32, 22, 32, 33, 34, 40, 38, 36, 29, 34, 24, 24, 39, 32, 37, 30, 20, 29, 26, 36, 40, 34, 22, 30, 27, 38, 27, 26, 28, 23, 40, 31, 22, 23, 35, 23, 31, 23, 39, 30, 20, 20, 35, 27, 23, 23, 29, 40, 20, 34, 40, 28, 25]
m4 =  50

votes5 =  [25, 25, 25, 24, 25, 24, 24, 25, 26, 25, 26, 24, 25, 26, 24, 26, 24, 26, 26, 25, 26, 24, 26, 24, 26, 26, 26, 25, 25, 26, 24, 26, 25, 25, 24, 25, 25, 26, 26, 26, 25, 26, 25, 26, 25, 25, 24, 24, 24, 25, 24, 26, 25, 24, 26, 24, 24, 26, 24, 26, 24, 24, 24, 26, 24, 25, 24, 26, 25, 25, 26, 25, 25, 25, 25, 26, 25, 24, 25, 25, 24, 24, 24, 26, 26, 26, 25, 24, 25, 25, 25, 26, 25, 24, 26, 24, 25, 26, 24, 26]
m5 =  50


print("winning is possible for votes1:", winnable(votes1,m1))
print()

print("winning is possible for votes2:", winnable(votes2,m2))
print()

print("winning is possible for votes3:", winnable(votes3,m3))
print()

print("winning is possible for votes4:", winnable(votes4,m4))
print()

print("winning is possible for votes5:", winnable(votes5,m5))
print()


```
