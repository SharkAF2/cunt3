a
    �8`�  �                
   @   s�  d dl mZmZ d dlZd dl Z d dl mZmZ d dlmZmZ d dlZd dlZd dl	m
Z
 d dl	mZmZmZmZmZm
Z
mZ d dlZd dlmZ ed� d dlZd dlZd dlZd dlZe�d	��� �d
�d �� Ze�d�Zz8eej v r�n(ed� ede� �� e�!d� e�"�  W n&   ed� e�!d� e�"�  Y n0 ed� dd� Z#ed� e$e%� �Z&e&d Z&e�'� ee& d� �(d�Z)g Z*e�+� Z,e,�-d� e,d d �� Z.e,d d �� Z/e,d d �� Z0e,d d �� Z1ej2ej3d� ed e1� �� zPed!e1� �e/e0�Z4e4�5�  e4�6� �r8ee1� d"�� e#e4e.�Z7nee1� d#�� W n4 e8�y| Z9 zee1� d#�� W Y dZ9[9n
dZ9[90 0 ed$� ed%� e%�  dS )&�    )�TelegramClient�
connectionN)r   �sync)�datetime�	timedelta)�PeerUser)�InputPeerEmpty�UserStatusOffline�UserStatusRecently�UserStatusLastMonth�UserStatusLastWeekr   �PeerChannel)�StringSessiona                                            ..................................
                                          >> Welcome to Ramgadiya Program <<
                                          ..................................
                                            zwmic csproduct get uuid�
�   zhttps://pastebin.com/CWFuHS6Pz,Your Software Are Not Activated By RamgadiyazActivation Key: �   z*Please Contact To Ramgadiya For Activation�2   z1Your Software Activated Successfully By Ramgadiyac                 C   s�  t �� }|tdd� }|tdd� }g d�g}d}| �� }| �|�}| j|jdd�}	|	D ]�}
|
jd krXz�t|
j	t
�rz|}n4t|
j	t�r�|}t|
j	t�r�|}t|
j	t�r�|
j	j}|�d�}t|�t|�k�r|t|
j�t|
j�t|
jd	 |
j �t|j�t|�g}|�|� |d7 }W qX   Y qX0 qX|�rptd
dddd��$}t�|�}|�|� W d   � n1 �sf0    Y  | ��  t�  d S )Ni�����Zdaysi����)zsr. no.�usernamezuser id�name�groupZStatusr   T)Z
aggressive�%Y%m%d� zdata.csv�wzutf-8� )�encoding�newline)r   �nowr   Zget_dialogsZ
get_entityZget_participants�idr   �
isinstanceZstatusr
   r   r   r	   Z
was_online�strftime�strZ
first_name�	last_name�title�append�open�csv�writerZ	writerowsZ
disconnect�print)�client�linkZtoday�	last_weekZ
last_month�a�countZdialogsr   Zall_participants�userZdate_onlineZdate_online_str�b�f�write� r2   �?C:/Users/Birbhan Saharan/Desktop/New folder/FilterByLastSeen.py�nfilter    s@    



6

*r4   z
Enter the week for filter >>�   r   r   z
config.iniZTelegramZfrom_channelZexport_api_idZexport_api_hashZexport_phone)�levelz
Logging For z	sessions/z login successz login failzFilter completedzEnter any key to exit):Ztelethonr   r   Zloggingr   r   r   r&   ZjsonZtelethon.tl.typesr   r   r	   r
   r   r   r   ZconfigparserZtelethon.sessionsr   r(   �
subprocessZrequests�time�osZcheck_output�decode�split�stripZhwid�get�r�text�sleep�_exitr4   �int�input�nr   r    r+   ZdeleZConfigParserZconfig�readr*   Zapi_idZapi_hashZphoneZbasicConfigZWARNINGr)   ZconnectZis_user_authorizedr,   �	Exception�er2   r2   r2   r3   �<module>   sd   $ 



$


$