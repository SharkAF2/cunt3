a
    ~n`�  �                
   @   s�  d dl mZ d dlmZ d dlZd dlmZ d dlZedd���LZdd� e�e�D �Z	d Z
e	D �]Ze�e�Ze
d	7 Z
ed
d��BZe�e�Zee�Zee
�Zd	Zeed	  ed	  ZW d  � n1 s�0    Y  ed
d��BZe�e�Zee�Zee
�ZdZeed	  ed	  ZW d  � n1 �s&0    Y  ee�Zee�Zede� �� ede� �ee�Ze�e� e��  e�  q^dZW d  � n1 �s�0    Y  ed� ed� e e�r�dnd� dS )�    )�TelegramClient)�utilsN)�readerz	phone.csv�rc                 C   s   g | ]}|d  �qS )r   � )�.0�rowr   r   �:C:/Users/Birbhan Saharan/Desktop/New folder/LoginNumber.py�
<listcomp>   �    r
   �   zapi.csv�   zLogin >> ! z	sessions/TzAll Number Login Done !a<                                            ................................................
                                           >> Thank You For Choosing Ramgadiya Program <<
                                          ................................................
                                            � zError!)!Ztelethon.syncr   Ztelethonr   Zcsvr   Zconfigparser�open�fZstr_listZpoZpphoneZparse_phoneZphoneZ
api_obj_idZ
csv_reader�listZlist_of_rows�intZ
row_numberZ
col_numberZdeltaopZhash_objZdeltaxdZapi_id�strZapi_hash�printZclient�startZ
disconnectZdone�inputr   r   r   r	   �<module>   sB   


2
4
$