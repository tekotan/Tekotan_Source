import numpy as np
import re
from random import randint
from mysite.settings import STATIC_URL
import os
#Importing Data
if os.path.isdir("tekotan.pythonanywhere.com/"):
    wordsList = np.load('tekotan.pythonanywhere.com/' + STATIC_URL + 'tensorboard/Numpy_Arrays/wordsList.npy')
    wordsList = wordsList.tolist()
    wordsList = [word.decode('UTF-8') for word in wordsList]
    wordVectors = np.load('tekotan.pythonanywhere.com/' + STATIC_URL + 'tensorboard/Numpy_Arrays/wordVectors.npy')
    strip_special_chars = re.compile("[^A-Za-z0-9 ]+")
else:
    wordsList = np.load('static/tensorboard/Numpy_Arrays/wordsList.npy')
    wordsList = wordsList.tolist()
    wordsList = [word.decode('UTF-8') for word in wordsList]
    wordVectors = np.load('static/tensorboard/Numpy_Arrays/wordVectors.npy')
    strip_special_chars = re.compile("[^A-Za-z0-9 ]+")
#Helper Functions
def cleanSentences(string):
    string = string.lower().replace("<br />", " ")
    return re.sub(strip_special_chars, "", string.lower())


# RNN Model

### Hyper Parameters

batchSize = 256
lstmUnits = 64
numClasses = 2
iterations = 75000
learning_rate = 0.001
maxSeqLength = 20
num_layers = 2

import tensorflow as tf
with tf.name_scope("Input_Data") as scope:
    labels = tf.placeholder(tf.float32, [batchSize, numClasses], name='Sentiment_Labels')
    input_data = tf.placeholder(tf.int32, [batchSize, maxSeqLength], name='Text')

with tf.name_scope("Data_Preprocessing") as scope:
    data = tf.Variable(tf.zeros([batchSize, maxSeqLength, 3]),dtype=tf.float32, name='Embed_Text')
    data = tf.nn.embedding_lookup(wordVectors,input_data)

with tf.name_scope("MultiRNN") as scope:
    def lstm():
        lstmCell1 = tf.nn.rnn_cell.LSTMCell(lstmUnits, initializer=tf.contrib.layers.xavier_initializer())
        lstmCell1 = tf.nn.rnn_cell.DropoutWrapper(cell=lstmCell1, output_keep_prob=0.9)
        return lstmCell1
    cell = tf.nn.rnn_cell.MultiRNNCell([lstm() for i in range(8)])
    value, _ = tf.nn.dynamic_rnn(cell, data, dtype=tf.float32)

    cell = tf.nn.rnn_cell.LSTMCell(lstmUnits)
    cell = tf.nn.rnn_cell.DropoutWrapper(cell, output_keep_prob=0.9)
    cell1 = tf.nn.rnn_cell.LSTMCell(lstmUnits)
    cell1 = tf.nn.rnn_cell.DropoutWrapper(cell1, output_keep_prob=0.9)

    (forward_output, backward_output), _ = \
        tf.nn.bidirectional_dynamic_rnn(cell, cell1, inputs=value, dtype=tf.float32,scope='BLSTM_1')
    value = tf.concat([forward_output, backward_output], axis=2)

value = tf.layers.dense(inputs=value, units=128, use_bias=True, kernel_initializer=tf.contrib.layers.xavier_initializer())
value = tf.nn.dropout(value, keep_prob=0.9)
value = tf.layers.dense(inputs=value, units=64, use_bias=True, kernel_initializer=tf.contrib.layers.xavier_initializer())
value = tf.nn.dropout(value, keep_prob=0.9)
value = tf.layers.dense(inputs=value, units=32, use_bias=True, kernel_initializer=tf.contrib.layers.xavier_initializer())
value = tf.nn.dropout(value, keep_prob=0.9)
value = tf.layers.dense(inputs=value, units=16, use_bias=True, kernel_initializer=tf.contrib.layers.xavier_initializer())
value = tf.layers.dense(inputs=value, units=8, use_bias=True, kernel_initializer=tf.contrib.layers.xavier_initializer())
value = tf.layers.dense(inputs=value, units=4, use_bias=True, kernel_initializer=tf.contrib.layers.xavier_initializer())

with tf.name_scope("Prediction_Parameters") as scope:
    weight = tf.Variable(tf.truncated_normal([4, numClasses]), name='Weights')
    bias = tf.Variable(tf.constant(0.1, shape=[numClasses]), name='bias')
    value = tf.transpose(value, [1, 0, 2])
    last = tf.gather(value, int(value.get_shape()[0]) - 1)
with tf.name_scope("Prediction") as scope:
    prediction = tf.nn.softmax(tf.matmul(last, weight) + bias)

with tf.name_scope("Accuracy") as scope:
    correctPred = tf.equal(tf.argmax(prediction,1), tf.argmax(labels,1))
    accuracy = tf.reduce_mean(tf.cast(correctPred, tf.float32))


with tf.name_scope("Loss") as scope:
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=prediction, labels=labels))
with tf.name_scope("Train") as scope:
    optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

import datetime
sess = tf.InteractiveSession()
tf.summary.scalar('Loss', loss)
tf.summary.scalar('Accuracy', accuracy)
merged = tf.summary.merge_all()
validation = tf.summary.scalar('Validation', accuracy)

sess = tf.InteractiveSession()
saver = tf.train.Saver()
sess.run(tf.global_variables_initializer())


# Training

import re
strip_special_chars = re.compile("[^A-Za-z0-9 ]+")

def cleanSentences(string):
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
def test(sent):
    x = ['positive', 'negative']
    sent = getSentenceMatrix(sent)
    pred = sess.run(prediction, {input_data:sent})[0]
    return(x[np.argmax(pred)])
def results():
    arr = np.array([[1, 0]], dtype=np.float32)
    arr_pred = np.array([test("my life sucks")])
    for i in range(1000000, ids.shape[0], batchSize):
        arr = np.vstack((arr, the_labels[i-batchSize:i]))
        arr_pred = np.vstack((arr_pred, sess.run(prediction, {input_data:ids[i-batchSize:i]})))
    x = np.argmax(arr_pred, axis=1)
    y = np.argmax(arr, axis=1)
    return((np.sum(np.equal(x, y))/x.shape))
sess = tf.InteractiveSession()
saver = tf.train.Saver()
if os.path.isdir("tekotan.pythonanywhere.com/"):
    saver.restore(sess, tf.train.latest_checkpoint('../'+STATIC_URL +'/tensorboard/RNN2'))
else:
    saver.restore(sess, tf.train.latest_checkpoint('C:/Users/btani/Google Drive/Work/Tekotan_git/Main/static/tensorboard/RNN2'))
