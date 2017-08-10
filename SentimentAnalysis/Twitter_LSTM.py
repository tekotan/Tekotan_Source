import numpy as np
import tensorflow as tf
import pandas as pd
import re
import datetime
from random import randint
wordsList = [word.decode('UTF-8') for word in (np.load('SentimentAnalysis/Numpy_Arrays/wordsList.npy').tolist())] #Encode words as UTF-8
wordVectors = np.load('SentimentAnalysis/Numpy_Arrays/wordVectors.npy')
text = np.load('SentimentAnalysis/Numpy_Arrays/text.npy')
the_labels = np.load('SentimentAnalysis/Numpy_Arrays/labels.npy')
ids = np.load('SentimentAnalysis/Numpy_Arrays/idsMatrix.npy')
print('Loaded everything')


def cleanSentences(string):
    strip_special_chars = re.compile("[^A-Za-z0-9 ]+")
    string = string.lower().replace("<br />", " ")
    return re.sub(strip_special_chars, "", string.lower())
def getSentenceMatrix(sentence):
    arr = np.zeros([batchSize, maxSeqLength])
    sentenceMatrix = np.zeros([batchSize,maxSeqLength], dtype='int32')
    cleanedSentence = cleanSentences(sentence)
    split = cleanedSentence.split()
    for indexCounter,word in enumerate(split):
        try:
            sentenceMatrix[0,indexCounter] = wordsList.index(word)
        except ValueError:
            sentenceMatrix[0,indexCounter] = 399999 #Vector for unkown words
    return sentenceMatrix
def getTrainBatch():
    label = []
    arr = np.zeros([batchSize, maxSeqLength])
    for i in range(batchSize):
        num = randint(1, 1000000)
        arr[i] = ids[num]
        label.append(the_labels[num])
    return arr, label
def getTestBatch():
    label = []
    arr = np.zeros([batchSize, maxSeqLength])
    for i in range(batchSize):
        num = randint(1000001, the_labels.shape[0]-1)
        arr[i] = ids[num]
        label.append(the_labels[num])
    return arr, label
def test(sent):
    x = ['positive', 'negetive']
    sent = getSentenceMatrix(sent)
    pred = sess.run(prediction, {input_data:sent})[0]
    return "{}".format(x[np.argmax(pred)])
    #return x[np.argmax(pred)]
def run(it=5):
    iterations = it
    su = 0
    li = []
    for i in range(iterations):
        nextBatch, nextBatchLabels = getTestBatch();
        su+=sess.run(accuracy, {input_data: nextBatch, labels: nextBatchLabels})
        li.append(sess.run(accuracy, {input_data: nextBatch, labels: nextBatchLabels}))

    x = np.array(li)
    s = pd.Series(x)
    print(s.describe())
    return(s.describe()[1])
def lstm():
    lstmCell1 = tf.contrib.rnn.BasicLSTMCell(lstmUnits)
    lstmCell1 = tf.contrib.rnn.DropoutWrapper(cell=lstmCell1, output_keep_prob=0.75)
    return lstmCell1
maxSeqLength = 20
batchSize = 192
lstmUnits = 64
numClasses = 2
iterations = 200000
num_layers = 3
learning_rate = 0.0005
maxSeqLength = 20
with tf.name_scope("Input_Data") as scope:
    labels = tf.placeholder(tf.float32, [batchSize, numClasses], name='Sentiment_Labels')
    input_data = tf.placeholder(tf.int32, [batchSize, maxSeqLength], name='Text')
with tf.name_scope("Data_Preprocessing") as scope:
    data = tf.Variable(tf.zeros([batchSize, maxSeqLength, 3]),dtype=tf.float32, name='Embed_Text')
    data = tf.nn.embedding_lookup(wordVectors,input_data)
with tf.name_scope("MultiRNN") as scope:
    multilayer = tf.contrib.rnn.MultiRNNCell([lstm() for i in range(num_layers)])
    value, _ = tf.nn.dynamic_rnn(multilayer, data, dtype=tf.float32)
with tf.name_scope("Prediction_Parameters") as scope:
    weight = tf.Variable(tf.truncated_normal([lstmUnits, numClasses]), name='Weights')
    bias = tf.Variable(tf.constant(0.1, shape=[numClasses]), name='bias')
    value = tf.transpose(value, [1, 0, 2])
    last = tf.gather(value, int(value.get_shape()[0]) - 1)
with tf.name_scope("Prediction") as scope:
    prediction = tf.nn.softmax(tf.matmul(last, weight) + bias)
with tf.name_scope("Accuracy") as scope:
    correctPred = tf.equal(tf.argmax(prediction,1), tf.argmax(labels,1))
    accuracy = tf.reduce_mean(tf.cast(correctPred, tf.float32))
with tf.name_scope("Loss") as scope:
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=labels))
with tf.name_scope("Train") as scope:
    optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

sess = tf.InteractiveSession()
saver = tf.train.Saver()
saver.restore(sess, tf.train.latest_checkpoint('SentimentAnalysis/tensorboard'))
