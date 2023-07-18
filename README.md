# NBA-MVP-Prediction-and-Historical-Analysis-Using-Cross-Era-Comparison
In this project, we develop machine learning models to predict the MVP of the NBA.
5 pre-defined models (SVM, ElasticNet, AdaBoost, GradientBoosting, Random Forest) were trained with specific parameters for this task.
Subsequently, we developed our own Neural Network MVPNet, which performed significantly better than the pre-existing models.
Next, we performed SHAP variable analysis to observe which features were most important to the model.
Finally, we used MVPNet to compare players of different eras, by adjusting their stats according to the pace of some era and then running them through our model.