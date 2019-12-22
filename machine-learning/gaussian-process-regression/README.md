<img src="http://sashagusev.github.io/images/plot_gp.svg" align="right" width="25%"/>

# Gaussian Process Regression

> IDE

![PyCharm](https://img.shields.io/badge/PyCharm-2019.3%20(Professional%20Edition)-brightgreen)
![Spyder](https://img.shields.io/badge/Spyder-4.0.0-red)
![PyTorch](https://img.shields.io/badge/PyTorch-1.3.1-red)
![gpytorch](https://img.shields.io/badge/gpytorch-0.3.6-green)
![Python](https://img.shields.io/badge/Python-3.7.5-blue)

<br/><br/>

**_Gaussian process regression_** (**_GPR_**) is a nonparametric, Bayesian approach to regression that is making waves in the area of machine learning. **_GPR_** has several benefits, working well on small datasets and having the ability to provide uncertainty measurements on the predictions.

### Background

Unlike many popular supervised machine learning algorithms that learn exact values for every parameter in a function, the Bayesian approach infers a probability distribution over all possible values. Let’s assume a linear function: y=wx+ϵ. How the Bayesian approach works is by specifying a prior distribution, p(w), on the parameter, w, and relocating probabilities based on evidence (i.e. observed data) using Bayes’ Rule:

![equation](https://miro.medium.com/max/2800/1*cQLU4V-WHi4xGS7MKGzR4g.png)
_Calculating posterior distribution with Bayes’ Rule_

The updated distribution p(w|y, X), called the posterior distribution, thus incorporates information from both the prior distribution and the dataset. To get predictions at unseen points of interest, x*, the predictive distribution can be calculated by weighting all possible predictions by their calculated posterior distribution:

![equation](https://miro.medium.com/max/2800/1*Se-i1g57jCoLy4EszR74hg.png)
_Calculating predictive distribution, f* is prediction label, x* is test observation_

The prior and likelihood is usually assumed to be Gaussian for the integration to be tractable. Using that assumption and solving for the predictive distribution, we get a Gaussian distribution, from which we can obtain a point prediction using its mean and an uncertainty quantification using its variance.

### Gaussian process regression
**_GPR_** is nonparametric (i.e. not limited by a functional form), so rather than calculating the probability distribution of parameters of a specific function, **_GPR_** calculates the probability distribution over all admissible functions that fit the data. However, similar to the above, we specify a prior (on the function space), calculate the posterior using the training data, and compute the predictive posterior distribution on our points of interest.

There are several libraries for efficient implementation of Gaussian process regression (e.g. scikit-learn, Gpytorch, GPy), but in order to understand 100% I'd implement every process using NumPy. At the end I'd use Gpytorch (0.3.6) Gaussian process package to compare my code.
