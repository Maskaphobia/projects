## Bezier curves 😎
**[Difficulty: 5/10]** <br>

**Bézier curves** are a more advanced technique for creating smooth, precise curves in Desmos. <br>

As they are just an approximation of a real world shape that has no mathematical representation or a representation that is unknown or too complicated, they are widely used in graphic design, animation, and computer graphics to create smooth curves.<br>

Although they might be hard to understand mathematically, it is easy to implement it! 

## Guide 

### What is a Bezier curve?
A Bezier curve is a smooth curve defined by a set of **control points**. There are different orders of Bezier curves depending on the number of control points. (Linear, Quadratic, Cubic) <br>
In Desmos, we mainly use **cubic Bezier curves** as they offer the most flexibility and control. 

### Implementing it
Formula: B(t) = (1-t)³P0 + 3(1-t)²tP1 + 3(1-t)t²P2 + t³P3 <br>
After defining 4 control points as coordinates, you can adjust the control points to change the shape of the curve. <br>

<img width="439" height="426" alt="image" src="https://github.com/user-attachments/assets/abacbed8-c01d-4d1a-afd4-b26bee512196" /> <br>

> Note: Bezier curves cannot be used for coloring as they are parametric ESTIMATION of a curve rather than a true mathematical equation. Use inequalities or polygons for filling areas instead 

## Reference and helpful links to explore further 
- [Orders of Bezier curves in Desmos](https://www.desmos.com/calculator/kkkramcrqj) 
- [How I animate stuff on Desmos Graphing Calculator](https://www.youtube.com/watch?v=BQvBq3K50u8) - If making one frame of a video is difficult enough, how did he animate a whole video? 
- [The Beauty of Bézier Curves](https://www.youtube.com/watch?v=aVwxzDHniEw&t) - Deeper understanding of the mathematics of bezier curves

---

## My attempt: 
<img width="736" height="943" alt="764cd752c23575a5ba2adebe3baad368" src="https://github.com/user-attachments/assets/052b062b-0212-4ed1-8703-559673b3f6ba" />


### Original photo


### My graph (~27 equations)
<img width="448" height="753" alt="image" src="https://github.com/user-attachments/assets/a54774ee-78f7-49d8-a2d8-80e48f99e9e3" /><br>
Link: https://www.desmos.com/calculator/efso3tcxuo 
