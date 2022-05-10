

**Image Tagging** 

**Introduction**  

` `An image tagging model was created to determine the colour and kind of women's clothing. Django was used to incorporate the model into a website.

**Data Creation** 

In a short amount of time, I created the data using the selenium a web scraping library. The extracted data was then saved in the form of a CSV file. 

**Colour detection** 

To efficiently detect colour in the image, I initially used the open cv grab cut technique to extract the foreground. 
![Aspose Words 0fb96eab-803c-40d2-98e8-1b1bfeeaf912 001](https://user-images.githubusercontent.com/86610832/167624599-fded92b4-8a03-4145-bfab-4af6866a58a3.png) ![Aspose Words 0fb96eab-803c-40d2-98e8-1b1bfeeaf912 002](https://user-images.githubusercontent.com/86610832/167624670-018f149c-89db-4f06-b3a7-0bee64085302.png)

Then I used k-means clustering to extract the image's top two colours, which were black and clothing colours. 
![Aspose Words 0fb96eab-803c-40d2-98e8-1b1bfeeaf912 003](https://user-images.githubusercontent.com/86610832/167625190-676236b2-1f8e-40a8-87a5-241c6fe7f49e.png)

The closest common colour is then determined using Euclidian distance. The closest colour in the above should be orange, and the results were also orange. 

*color\_detection.ipynb* contains code for above process 

**Dress type classification** 

Six separate classes of dress were classified in the dress type classification. I trained the model Xception for 5 epochs at a batch size of 32, which resulted in a 94 per cent accuracy. 

Classes -: kurta, saree, lehenga, top, dress, shirt. Dress\_type\_classification.ipynb contains code for above process. 

**Website** 

The website was made with the help of Django and bootstrap. It was built around the models. So anytime the user uploads the image the dress colour and its type is presented to the user. 

See ***sample\_video.mp4*** for the website demo. The Screen Recording was not able to fully capture. 

**Conclusion and Future Work -:** 

The dress categorization algorithm performed admirably, but it had not been tested on data from other e-commerce platforms such as Amazon, Flipkart, and others. Color detection worked well in general, although it made mistakes in some images, which might be improved by employing deep learning models instead of KNN. 

We can enhance the accuracy of dress classification by using the Deep Convolutional Generative Adversarial Network to augment the data, and we can improve the accuracy even more by passing the extracted foreground instead of the entire image. Integrating data from numerous e-commerce platforms is another approach to improve accuracy. 
