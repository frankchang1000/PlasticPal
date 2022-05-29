<p align="center">
  <img src="https://github.com/frankchang1000/Poolesville/blob/main/docs/logo.png", width="150"/>
</p>

# PlasticPal

Promoting **proper** recycling with advanced AI through a multiplatform app.

## Table of Contents 📑

* [Purpose and Inspiration](#purpose-and-inspiration)
* [What it does](#what-it-does)
* [Installation and Usage](#installation-and-usage)
* [How we built it](#how-we-built-it)
* [Challenges we ran into](#challenges-we-ran-into)
* [Accomplisments we're proud of](#accomplishments-were-proud-of)
* [What we learned](#what-we-learned)
* [What's next for PlasticPal](#whats-next-for-plasticpal)
* [References](#references)
* [License](#license)

## Purpose and Inspiration 💡

<p align="center">
  <img src="https://github.com/frankchang1000/Poolesville/blob/main/docs/waste_statistics.png", width="500"/>
</p>

According to the Environmental Protection Agency, almost 300 million tons of waste are produced by the United States per year. Trash can take decades to decompose, especially as more and more garbage is piled onto landfills. Around 20% of the 300 million tons of trash are recycled, but most of the recycling is done incorrectly. Improper recycling can not only reduce the efficiency of recycling, but it can also harm the environment by releasing toxic chemicals. Plastic Pal aims to promote proper recycling through the use of neural networks.

## What it does ❓

<p align="center">
  <img src="https://github.com/frankchang1000/PlasticPal/blob/main/docs/slides/07.png", width="500"/>
</p>

PlasticPal uses computer vision to determine if an item is recyclable. Then, our end-user can properly dispose of the item, helping to improve the environment and our recycling conditions.

Plastic Pal takes an image from a camera input, and feeds the image to our EfficientNet model. The neural network classifies the image into one of 101 different categories, and is able to determine if the waste is fully recyclable, is only partly recyclable, or if it should not be recycled at all. Visual infographics are also displayed in order to easily inform the user of the reasoning behind the decision.

## Installation and Usage ⌨️🖱️

To use begin with cloning the repository from GitHub, install the requirments, and run the Streamlit application.

```cmd
git clone https://github.com/frankchang1000/PlasticPal.git
python -m venv venv 
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
streamlit run main.py
```

### Tensorflow GPU Support 💻

To utilize the GPU for AI processing download the proper drivers for your model of GPU. If your GPU has a compute capability of at least 7.0, you can use mixed precision inference; otherwise, you can use float32. Any RTX card should support this feature.

We utilized Tensorflow 2.9 which requires the latest version of the drivers for your Nvidia GPU.

## How we built it ⚙️🔧

<p align="center">
  <img src="https://github.com/frankchang1000/PlasticPal/blob/main/docs/slides/09.png", width="500"/>
</p>

Our backend is powered using the most recent version of Tensorflow, Tensorflow2.9. We incorporated optimizations to our backend server including mixed precision training and inference. Our neural network (EfficientNetv2) was slightly modified to be wider than normal to increase pattern recognition, and improve inference. The results were a resounding 95% accuracy on our private test set. Lastly, we utilized numerous web scraping techniques to advance, improve, and clean our large training dataset with over 10000 images. PlasticPal uses the most advanced technology available to solve the world’s leading problems.

The front-end was built with Streamlit and Python, and uses a multi-page setup in order to have one page for initial camera scanning, and a final decision page. Once the classification is made, we pull the recycling status key from a dictionary and print out the final verdict. We also display an infographic depending on the recycling status.

## Challenges we ran into 👷‍♂️

At first, we attempted to web scrape the different recycling categories for each type of waste from a website, but we faced many challenges as the website’s language was chinese. We tried applying the GoogleTranslate API to pull the html data and translate it, but did not meet much success. We also wanted our front end to switch pages when the user took a picture, but Streamlit was unable to support this feature. We resorted to a dropdown menu which was more widely documented by the Streamlit users.

## Accomplishments that we're proud of 🎉

PlasticPal achieved an extremely high classification accuracy with almost 95% during training. Our model was able to accurately predict from the camera stream unlike our previous hackathon projects. Although our front-end is still not perfect, our skills in UI and front-end execution have shown great improvement.

Our code management was also amazing in this project, as we created many folders for better organization. Our programs are well formatted, making for easy debugging as well as easy collaboration between multiple people working on the same file.

## What we learned 📚

Along with new techniques for creating efficient and accurate neural networks, we also learned important skills for data preprocessing. We learned how to pull keys from a dictionary, and how to convert those camelcase keys to normal human text using APIs such as inflection. We have used streamlit before, but this time we learned how to create multi page apps to improve user accessibility and clarity.

## What's next for PlasticPal 🚀

In the future, we hope to extend the classification complexity of PlasticPal to the different recycling numbers as well. Each number has a very specific material, and recycling methods only work for some of these materials. This would require a larger dataset with labels corresponding to the material, so that the neural network can learn the features of each type of plastic.

## References

[1] Tan, M., & Le, Q. (2019, May). Efficientnet: Rethinking model scaling for convolutional neural networks. In International conference on machine learning (pp. 6105-6114). PMLR.

## License

MIT License (MIT) Copyright (c) 2022 frankchang1000, IdeaKing, and the contributors.
