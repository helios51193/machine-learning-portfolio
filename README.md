# Machine Learning Portfolio

portfolio includes projects that i have done as a part of academic course and for self learning.

## Project 1 - Investment Analysis

#### Problem Statement
Spark Funds, an asset management company, wants to make investments in a few companies. The CEO of Spark Funds wants to understand the global trends in investments so that she can take the investment decisions effectively.

#### Objective
The main objective of the problem is to analyse the data and give answers to the following questions.
* What type of investment is suitable for the company (venture, angel, seed, and private equity) ?
* Which Country and Sector will be suitable for investment ?
* Selecting top 3 English-speaking Countries for the above selected countries.

## Project 2 - Lending Club Case Study

#### Problem Statement
You work for a consumer finance company which specialises in lending various types of loans to urban customers. When the company receives a loan application, the company has to make a decision for loan approval based on the applicant’s profile. 

#### Objective

The main objective of the case study is to perform EDA the loan dataset and find out potential risk factors that may lead to defaulting a loan.

## Project 3 - Car Price Prediction using Linear Regression

#### Problem Statement

A Chinese automobile company Geely Auto aspires to enter the US market by setting up their manufacturing unit there and producing cars locally to give competition to their US and European counterparts. 

#### Objective

We are given a dataset containing information about US cars .We have to identify important features using EDA and create a model using linear regression that will predict the car prices for the company.

## Project 4 - House Price Prediction using Regularized Regression

#### Problem Statement

A US-based housing company named Surprise Housing has decided to enter the Australian market. The company uses data analytics to purchase houses at a price below their actual values and flip them on at a higher price. 

### Objective

The company is looking at prospective properties to buy to enter the market. You are required to build a regression model using regularisation in order to predict the actual value of the prospective properties and decide whether to invest in them or not.

## Project 5 - Telecom Churn Case Study

#### Problem Statement

In the telecom industry, customers are able to choose from multiple service providers and actively switch from one operator to another. In this highly competitive market, the telecommunications industry experiences an average of 15-25% annual churn rate. Given the fact that it costs 5-10 times more to acquire a new customer than to retain an existing one, customer retention has now become even more important than customer acquisition.

### Objective
Main objectives are as follows.
1. Identify the high value customers.In this case study, high-value customer is based on revenue i.e. the top 20% customers which generate the highest revenue.
2. Identify the churn factors and build a model to classify whether a customer is a potential churn customer.

## Project 6 - Vitterbi Algorithm

#### Problem Statement

You have learnt to build your own HMM-based POS tagger and implement the Viterbi algorithm using the Penn Treebank training corpus. The vanilla Viterbi algorithm we had written had resulted in ~87% accuracy. The approx. 13% loss of accuracy was majorly due to the fact that when the algorithm encountered an unknown word (i.e. not present in the training set, such as 'Twitter'), it assigned an incorrect tag arbitrarily. This is because, for unknown words, the emission probabilities for all candidate tags are 0, so the algorithm arbitrarily chooses (the first) tag.

#### Objective 

Modify the vitterbi algorithm to compensate the 13% loss of the accuracy due to unknown words.Explore atleast two approaches to solve the problem of unknown words.

## Project 7 - Chatbot with Rasa

#### Problem Statement

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. You have been hired as the lead data scientist for creating this product.

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.

#### Objective

Build and train a chat bot using the open source conversation AI Rasa.The bot should give recommendations of restaurants bases on the following questions.
1. City 
2. Cuisine 
3. Budget for 2.

The Bot should also be able to send top 10 restaurant to the person via email.

## Project 8 - Neural Network using Numpy

#### Problem statement

In this project, you will build a complete neural network using Numpy. You will implement all the steps required to build a network - feedforward, loss computation, backpropagation, weight updates etc.

#### Objective

The project is divided in to 6 parts.

1.Data Preparation
2.Feedforward
3.Loss Computation
4.Backpropogation
5.Parameter updates
6.Model Training and prediction.

We have to fill the each part with the appropriate code and formulas.


## Project 9 - Gesture Recognition using CNN and RNN

#### Problem Statement
Imagine you are working as a data scientist at a home electronics company which manufactures state of the art **smart televisions**. You want to develop a cool feature in the smart-TV that can **recognise five different gestures** performed by the user which will help users control the TV without using a remote

#### Objective
Create and train a model to recognize 5 types of gestures using the following two types of Neural Network
1. 3D CNN
2. CNN + RNN

## Project 10 - Numerical Tic-Tac-Toc using Q-learning

#### Problem Statement
One of the most popular and enduring games of all time is **[Tic-Tac-Toe](https://www.youtube.com/watch?v=5SdW0_wTX5c)**. Because of its familiarity, this game is often used as a starting example to mathematically analyze a decision-making process. Its brevity makes it a perfect game to illustrate the rewards of thinking ahead and learning the consequence of each decision.
Numerical tic-tac-toe is a variant of the basic tic-tac-toe. Instead of X’s and O’s, the numbers 1 to 9 are used. In the 3x3 grid, numbers 1 to 9 are filled, with one number in each cell. The first player plays with the odd numbers, the second player plays with the even numbers, i.e. player 1 can enter only an odd number in the cell while player 2 can enter an even number in one of the remaining cells.

#### Objective
Train an agent to play numerical tic-tac-toe using Q-learning algorithm. Rules of the game is as follows

1.  The game will be played on a 3x3 grid (9 cells) using numbers from 1 to 9. Each number can be used exactly once in the entire grid.
2.  There are two players: one is the Reinforcement Learning (RL) agent and other is the environment.
3.  The RL agent is given odd numbers {1, 3, 5, 7, 9} and the environment is given the even numbers {2, 4, 6, 8}  
4.  Each of them takes a turn. The player with odd numbers always goes first.
5.  At each round, a player puts one unused number on a blank spot.
6.  The objective is to make 15 points in a row, column or a diagonal. The player can use the opponent's numbers in the grid to make 15.
7.  The game terminates when any one of the players makes 15.

The agent will get 10 points if it wins,0 if the game draws.-1 for every move made.

## Project 11 - RL-based system for assisting cab drivers

#### Problem Statement
You are hired as a Sr. Machine Learning Er. at SuperCabs, a leading app-based cab provider in a large Indian metro city. In this highly competitive industry, **retention** **of good cab drivers** is a crucial business driver, and you believe that a sound **RL-based system for assisting cab drivers** can potentially retain and attract new cab drivers.

#### Objective

Train a vanilla DQN network which helps cab drivers to choose the 'right' rides for maximizing profit.

## Project 12 - EDA on Food Prices

#### Problem Statement
In 2022, the world may face a global food crisis. This dataset includes information on food prices, meat prices, dairy prices, cereal prices, oil prices, and sugar prices. This data is of utmost importance to researchers as it will help inform their work on finding solutions to this potential crisis. With this data, we can better understand the factors that may contribute to the crisis and work towards finding solutions that could help prevent or mitigate its effects.

#### Objective
Objective is to find trends in the dataset 

## Project 13 - Bajaj Allianz Hackthon

https://www.kaggle.com/competitions/allianz-hackathon

#### Objective

1. Train a model to predict the policy preferences of the customer.
2. Identify customer segments based on their personas and different market factors based on the decision

## Capstone - Style Transfer using GAN

#### Problem Statement
Misdiagnosis in the medical field is a very serious issue but it’s also uncomfortably common to occur. Imaging procedures in the medical field requires an expert radiologist’s opinion since interpreting them is not a simple binary process ( Normal or Abnormal). Even so, one radiologist may see something that another does not. This can lead to conflicting reports and make it difficult to effectively recommend treatment options to the patient.

One of the complicated tasks in medical imaging is to diagnose MRI(Magnetic Resonance Imaging). Sometimes to interpret the scan, the radiologist needs different variations of the imaging which can drastically enhance the accuracy of diagnosis by providing practitioners with a more comprehensive understanding.


But to have access to different imaging is difficult and expensive. With the help of deep learning, we can use style transfer to generate artificial MRI images of different contrast levels from existing MRI scans. This will help to provide a better diagnosis with the help of an additional image.


In this capstone, you will use CycleGAN to translate the style of one MRI image to another, which will help in a better understanding of the scanned image. Using GANs you will create T2 weighted images from T1 weighted MRI image and vice-versa.

#### Objective
To build a Generative adversarial model(modified U-Net) which can generate artificial MRI images of different contrast levels from existing MRI scans.




