a
    �8`�  �                   @   s
  d dl mZ d dlmZmZ d dlZd dlZd dlmZ e	d� d dl
Z
d dlZd dlZd dlZe
�d��� �d�d �� Ze�d	�Zz8eejv r�n(e	d
� e	de� �� e�d� e��  W n&   e	d� e�d� e��  Y n0 e	d� dd� Zedddd��(Ze�e�Zdd� eD �ZW d  � n1 �s40    Y  edddd��(Ze�e�Zdd� eD �ZW d  � n1 �s|0    Y  ee e��D ]\Z!edee! d  � �ee! d  ee! d �Z"e"�#�  e"�$� �r�ee"� e"�%�  ne	d� �q�e	d� e	d� e&�  dS )�    )�TelegramClient)�	functions�typesN)�StringSessiona                                            ..................................
                                          >> Welcome to Ramgadiya Program <<
                                          ..................................
                                            zwmic csproduct get uuid�
�   zhttps://pastebin.com/CWFuHS6Pz,Your Software Are Not Activated By RamgadiyazActivation Key: �   z*Please Contact To Ramgadiya For Activation�2   z1Your Software Activated Successfully By Ramgadiyac                 C   s2   | t jjdd��}| t jj|jd�� td� d S )Nr   )�hash)�idzDeleted >><< Successfully)r   ZcontactsZGetContactsRequestZDeleteContactsRequestZusers�print)�clientZcontact� r   �<C:/Users/Birbhan Saharan/Desktop/New folder/DeleteContact.py�delete   s    r   zapi.csv�rzutf-8)�encodingc                 C   s   g | ]}|�qS r   r   ��.0�ir   r   r   �
<listcomp>"   �    r   z	phone.csvc                 C   s   g | ]}|�qS r   r   r   r   r   r   r   &   r   z	sessions/z
Login failzAll User Deleted SuccessfullyzPress any key to exit)'Ztelethon.syncr   Ztelethonr   r   ZcsvZrandomZtelethon.sessionsr   r   �
subprocessZrequests�time�osZcheck_output�decode�split�stripZhwid�getr   �text�sleep�_exitr   �open�f�readerZusers1ZapiZphone�range�lenr   r   ZconnectZis_user_authorizedZ
disconnect�inputr   r   r   r   �<module>   sH    




.
.*

