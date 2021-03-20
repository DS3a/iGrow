# Welcome to iGrow

## Due to the pandemic, our team could not get together to build iGrow. 
### So we have done our best to simulate as many aspects of the machine that we could.

You can view the 3D model, which was built using Fusion 360 in the folder named "iGrow Design (fusion 360)"
If you don't have fusion you can view the model over here : https://a360.co/3f2D6pQ 
(we recommend using the Fusion 360 app for better performance, and accuracy.
The web app provided by Fusion 360 doesn't render the model properly)
The sensors on iGrow are <talk about sensors, and how we plan on maintaining the atmosphereic conditions required to grow the plant>


the sensor outputs, and other things were simulated using a random generator from numpy in the project called grover.
You can view the source code, and run it if you want in the folder called grover, 

### make sure, you use the virtual environment /dashboard/venv while using grover, and dashboard
assume that the grover app is the raspberry pi on iGrow, which collects all the values from the various sensors on the machine,
and sends it to the web app, called dashboard.

dasboard is a django app, which displays all the sensor values, and the ideal conditions for the growth of each plant from it's database.
you can choose which plant you want to grow, and iGrow will modify the atmospheric conditions inside of itself to ensure that the plant
is healthy, unfortunately, we couldn't simulate the live telecast from the camera atop iGrow.
For now, we just pulled the data off of a youtube link, and a kaggle site for the growth monitoring, and the disease detection repectively.

Disease Detection: https://www.kaggle.com/jarvis705/tomato-leaf-disease
Timelapse of plant growth: https://www.youtube.com/watch?v=-vffKB8ma7Q

The growth detection model is stored in plant_growth_detection. You may view the jupyter notebook, and the docstrings
to gain insights on how it works. Basically it counts all the green pixels in the image. We don't have to worry about background noise
as it is a very controlled environment, and no green light can seep in, except for if we want it to be green, 
then we can apply filters to get the desired output.
the output is displayed in evaluating_growth_detection_model.ipynb



In order to detect diseases, we created multiple models, and have evaluated them,
you can view the evaluations in disease_detection_tomato/eval_model.ipynb and disease_detection_tomato/eval_model_diff.ipynb
in order to see the training, checkout disease_detection_tomato/training_model.ipynb. We experimented with many models, 
some which were too complex and were taking a lot of time to train. infact, they were too large to upload onto github
you may view those models in the link given below.
Super Complex DL Models: https://drive.google.com/drive/folders/1NauM36ZngfZAMI7ig_diRrw8csSYH3A4?usp=sharing
We created simpler models to train, and got test accuracy scores upto 97%
Those models are in the repository, and in the training notebook as well.
