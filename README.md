# NBA_Weight_Height_Distribution
A small study to check how the Weight and Height standards have changed over the years. 


More specifically the goal was to see how weights and heights have changed throughout the last 20 years, to understand how teams change their perspective as the game evolves. 

The main reason for this study has been the constant evolution of the Center position (From the heavy and slow Roy Hibberts of this world to the more agile and light Jarret Allens) and the extinction of really small explosive guards (Isaiah Thomas might be the last of his kind).

#Checking Weight Distribution

Regarding the weights (in KGs) we split the datasets in 3 different timelines for 3 indicative timelines(the 0s, 10s and 20s).

More specifically the 3 timelinesare:
1. 2005-07
2. 2012-14
3. 2022-24

Using KDEplots we got the following distributions (For all positions):
![image](https://github.com/user-attachments/assets/1c3c2003-2310-4aa7-8698-ead4e934a82b)

We can't make a conclusion on this one, rather than it seems that the weights nowadays gathr around mostly around 95 kilograms. 

So we will split based on postitions:
In the following graphs i have merged the graphs together and split them to have a full perspective.

-Guards:
![image](https://github.com/user-attachments/assets/6382b526-d434-41e2-9126-c90a83f0e99d)
![image](https://github.com/user-attachments/assets/84e6f2db-80f4-4101-90ed-a526269f7e25)

-Forwards:
![image](https://github.com/user-attachments/assets/794755f0-6b61-4149-922f-33a7297f733b)
![image](https://github.com/user-attachments/assets/75775aa1-1de1-494c-a9df-96f84bed24a5)

-Centers:
![image](https://github.com/user-attachments/assets/06d5c957-2aca-4f3b-ade1-b7f8878c7bfd)
![image](https://github.com/user-attachments/assets/d7479a20-f2b4-4499-ab56-7da150995f99)


Some conclusions and observations:

-There were 60 kg guards(!!) (hadn't saved the names of players unfortunately, but i could come to update that info at a later time)
-Guards today range mostly from 80-100 kgs, with the distribution focusing more on 90 as years go by , indicating that this is the ideal weight for an NBA guard. 
-KDEplot suggest a change in the forwardx positions. 2005-07 forwards were mostly at around 105 kgs, while almost 2 decades later that number has dropped to around 5 kgs less (distribution focuses on 100 kgs today). So forwards are lighter today, aligning with the speed that the game require nowadays.
-Centers are lighter too today! In today's game centers don't go above 140kgs (while earlier there were examples of over 150 and 160 kilos)

A clearer picture can be given using boxplots for each position.

![image](https://github.com/user-attachments/assets/d78d7fc8-fcb8-466a-b535-fc7367b315dc)

From the boxplot it becomes clear, that forwards and centers tend to weight less today, while the guards weight seem to deviate less today and concentrating at around 90kgs. 


Small note:
All the data were extracted from the (fantastic) NBA_API.
