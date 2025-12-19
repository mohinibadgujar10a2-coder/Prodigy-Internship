# Prodigy-Internship
This repository implements two core Artificial Intelligence tasks showcasing statistical and deep learning approaches to generative modeling. It includes text generation using Markov Chains and image generation through Neural Style Transfer, demonstrating practical applications of AI in NLP and computer vision.

**Text Generation with Markov Chains | Task-03**

This project implements a simple text generation algorithm using Markov Chains. The model learns statistical patterns from a given text corpus and generates new text by predicting the next word based on the previous word(s).

**Objective**
To build a probabilistic text generation model that predicts the likelihood of a word occurring based on the preceding word(s) using Markov chains.

**Technologies Used**
Python
Standard Libraries (random, collections)

**How It Works**
The input text is tokenized into words.
A Markov chain model is built by storing transition probabilities between consecutive words.
The model randomly selects the next word based on learned probabilities.
Generated text follows similar patterns and structure as the training data.
 
**Project Structure**
Text-Generation-Markov-Chains/
│── input.txt
│── markov_text_generator.py
│── README.md

**Input**
Text corpus (any plain text file such as stories, articles, or paragraphs)

**Output**
Automatically generated text that mimics the style and structure of the input text.


**Neural Style Transfer | Task-05**
This project demonstrates Neural Style Transfer, a deep learning technique that blends the content of one image with the artistic style of another image (such as a famous painting). The implementation uses a pre-trained VGG19 convolutional neural network to extract content and style features and generates a stylized image through optimization.

**Objective**
To apply the artistic style of a given image to the content of another image using neural networks while preserving the original structure of the content image.
Technologies Used
Python
TensorFlow / Keras
NumPy
Matplotlib
Pre-trained VGG19 Model

**How It Works**
The content image provides the structure of the output.
The style image provides texture, color, and artistic patterns.
Style and content features are extracted using VGG19.
A new image is iteratively optimized to minimize content loss and style loss.
The final output is a visually appealing stylized image.

**Input**
Content Image (photo or scene)
Style Image (artwork or painting)

**Output**
A generated image that combines the content of one image with the artistic style of another.

**Project Structure**
Neural-Style-Transfer/
│── content.jpg
│── style.jpg
│── output.jpg
│── neural_style_transfer.ipynb
│── README.md

**Conclusion**
This project showcases how deep learning can be used creatively to merge art and technology, producing visually striking results through Neural Style Transfer.
