from time import sleep
from clear import clear
from score import score_calculator
def quiz():
    score = 0
    print("1. High entropy means that the partitions in classification are")
    print("a) pure \nb) not pure \nc) useful\nd) useless")
    answer1 = input("Enter Answer: ").strip().lower()
    sleep(1)
    if answer1 == "b":
        print("Correct!")
        score += 1 
    else:
        print("Oops! You are wrong :(")
    sleep(2)
    clear()
    print("Answer: (b) Not pure")
    sleep(1)
    print("Entropy is a measure of the randomness in the information being processed. The higher the entropy, the harder it is to draw any conclusions from that information.")
    sleep(1)
    print("It is a measure of disorder or purity or unpredictability or uncertainty.")
    sleep(1)
    print("Low entropy means less uncertain and high entropy means more uncertain.")
    sleep(2)
    clear()
    print("2. A machine learning problem involves four attributes plus a class. The attributes have 3, 2, 2, and 2 possible values each. The class has 3 possible values. How many maximum possible different examples are there? ")
    print("a) 12 \nb) 24 \nc) 48\nd) 72")
    answer2 = input("Enter Answer: ").strip().lower()
    sleep(1)
    if answer2 == "d":
        print("Correct!")
        score += 1 
    else:
        print("Oops! You are wrong :(")
    sleep(2)
    clear()
    print("Answer: (d) 72")
    sleep(1)
    print("Maximum possible different examples are the products of the possible values of each attribute and the number of classes;")
    sleep(1)
    print("3 * 2 * 2 * 2 * 3 = 72")
    sleep(2)
    clear()
    print("3. Which of the following is NOT supervised learning?")
    print("a) PCA \nb) Decision Tree \nc) Linear Regression\nd) Naive Bayesian")
    answer3 = input("Enter Answer: ").strip().lower()
    sleep(1)
    if answer3 == "a":
        print("Correct!")
        score += 1 
    else:
        print("Oops! You are wrong :(")
    sleep(2)
    clear()
    print("Answer: (a) PCA")
    sleep(1)
    print("Principal Component Analysis (PCA) is not predictive analysis tool. It is a data pre-processing tool. It helps in picking out the most relevant linear combination of variables and use them in our predictive model.")
    sleep(1)
    print("PCA is a technique for reducing the dimensionality of large datasets, increasing interpretability but at the same time minimizing information loss.")
    sleep(1)
    print("Supervised learning")
    sleep(1)
    print("Supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs. It infers a function from labeled training data consisting of a set of training examples.")
    sleep(1)
    print("Unsupervised learning")
    sleep(1)
    print("Unsupervised learning is a type of machine learning task where you only have to insert the input data (X) and no corresponding output variables are needed (or not known). It does not have labeled data for training. Algorithms are left to their own devices to help discover and present the interesting structure that is present in the data.")
    sleep(2)
    clear()
    print("4. Which of the following statements about Naive Bayes is incorrect?")
    print("a) Attributes are equally important. \nb) Attributes are statistically dependent of one another given the class value. \nc) Attributes are statistically independent of one another given the class value.\nd) Attributes can be nominal or numeric")
    answer4 = input("Enter Answer: ").strip().lower()
    sleep(1)
    if answer4 == "b":
        print("Correct!")
        score += 1 
    else:
        print("Oops! You are wrong :(")
    sleep(2)
    clear()
    print("Answer: (b) Attributes are statistically dependent of one another given the class value")
    sleep(1)
    print("Attributes are statistically independent of one another given the class value.")
    sleep(1)
    print("Naïve Bayes")
    sleep(1)
    print("Naïve Bayes classifier assumes conditional independence between attributes and assigns the MAP class to new instances.")
    sleep(1)
    print("Naive Bayes is a classification algorithm for binary (two-class) and multi-class classification problems. The technique is easiest to understand when described using binary or categorical input values.")
    sleep(1)
    print("It is called naive Bayes because the calculation of the probabilities for each hypothesis are simplified to make their calculation tractable. Rather than attempting to calculate the values of each attribute value P(d1, d2, d3|h), they are assumed to be conditionally independent given the target value and calculated as P(d1|h) * P(d2|H) and so on.")
    sleep(2)
    clear()
    print("5. Suppose we would like to perform clustering on spatial data such as the geometrical locations of houses. We wish to produce clusters of many different sizes and shapes. Which of the following methods is the most appropriate?")
    sleep(1)
    print("a) Decision Trees \nb) Density-based clustering \nc) Model-based clustering\nd) K-means clustering")
    answer5 = input("Enter Answer: ").strip().lower()
    if answer5 == "b":
        print("Correct!")
        score += 1 
    else:
        print("Oops! You are wrong :(")
    sleep(1)
    clear()
    print("Answer: (b) Density-based clustering")
    sleep(1)
    print("The density-based clustering methods recognize clusters based on density function distribution of the data object. For clusters with arbitrary shapes, these algorithms connect regions with sufficiently high densities into clusters.")
    sleep(2)
    clear()
    score_calculator(score)

if __name__ == "__main__":
    quiz()