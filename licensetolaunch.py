{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "3 4 1 7 2\n",
      "1\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "\n",
    "j = [int(x) for x in input().split()]\n",
    "\n",
    "t = min(j)\n",
    "\n",
    "i = j.index(t)\n",
    "\n",
    "#print(t)\n",
    "print(i)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
