a
    �8`x  �                   @   s@  d dl mZ d dlmZ d dlmZmZmZmZ d dl	m
Z
mZmZmZ d dlmZ d dlmZmZ d dlmZmZmZmZ d dlZd dlZd dlZd d	lmZ d dlZd dlZd dlZd d
lmZ d d
lmZ e d� d dl!Z!d dl"Z"d dlZd dl#Z#e!�$d��%� �&d�d �'� Z(e"�)d�Z*z:e(e*j+v �r.n(e d� e de(� �� e�,d� e#�-�  W n&   e d� e�,d� e#�-�  Y n0 e d� e�.� Z/e/�0d� e/d d Z1e2dd��<Z3ee3�Z4e5e4�Z6dZ7dZ8e6e7d  e8d  Z9W d  � n1 �s�0    Y  e:e9�Z;e;d a<e2dd��<Z=ee=�Z4e5e4�Z6e;Z7dZ8e6e7d  e8d  Z>W d  � n1 �s\0    Y  e2dd��<Z?ee?�Z4e5e4�Z6e;Z7dZ8e6e7d  e8d  Z@W d  � n1 �s�0    Y  e2dd��<Z3ee3�Z4e5e4�Z6e;Z7dZ8e6e7d  e8d  ZAW d  � n1 �s0    Y  e:e@�ZBeCeA�ZDe>ZEdaFdd � ZGeG�  dS )!�    )�TelegramClient)�GetDialogsRequest)�InputPeerEmpty�InputPeerChannel�InputPeerUser�PeerUser)�PeerFloodError�UserPrivacyRestrictedError�ChatWriteForbiddenError�UserAlreadyParticipantError)�InviteToChannelRequest)�GetFullChannelRequest�JoinChannelRequest)�types�utils�errors�	functionsN)�reader)�StringSessiona                                            ..................................
                                          >> Welcome to Ramgadiya Program <<
                                          ..................................
                                            zwmic csproduct get uuid�
�   zhttps://pastebin.com/CWFuHS6Pz,Your Software Are Not Activated By RamgadiyazActivation Key: �   z*Please Contact To Ramgadiya For Activation�2   z1Your Software Activated Successfully By Ramgadiyaz
config.iniZTelegram�	last_name�
memory.csv�rz	phone.csvzapi.csv�   ZDOc                  C   sD  t �t�} td| � �tt�}|��  |�� sNtd� |�	| � |�
| td�� d}g }t|dd��v}tj|ddd	�}t|d � |D ]F}i }|d
 |d< |d |d< t|d �|d< |d |d< |�|� q�W d   � n1 s�0    Y  tdd��<}t|�}	t|	�}
d}d}|
|d  |d  }W d   � n1 �s60    Y  t|�}|d }tdd��<}t|�}	t|	�}
d}d}|
|d  |d  }W d   � n1 �s�0    Y  t|�}|d }tdddd��0}tj|ddd	�}|�t||g� W d   � n1 �s�0    Y  d
}|D �],}t|�t|d �k�r�t|d �t|�k�r�z^|d7 }d}|d dk�rltd� W �q|tjj|d |d tt�ddd�� d|� d�}W nP tj�y� } z|jj}W Y d }~n*d }~0    t� �  td� Y �qY n0 t|� � n>t|d �t|�k�rtd� td�}|d k�r6t!�  nt"�  �qd S )!Nz	sessions/zsome thing has changedzEnter the code: zdata.csvzUTF-8)�encoding�,r   )Z	delimiterZlineterminatorr   Zsrnor   Zusernamer   �id�   �namer   r   �P   �w�delta� zno username, moving to nextZgdfT)r   Z
first_namer   �phoneZadd_phone_privacy_exceptionz - SavedzUnexpected ErrorzMembers Added Successfully!zRDone!
Choose From Below:

1 - Repeat The Script
OR Just Hit Enter To Quit

Enter: �1)#r   Zparse_phone�pphoner   �api_id�api_hashZconnectZis_user_authorized�printZsend_code_requestZsign_in�input�open�csvr   �next�int�append�list�writerZwriterow�	nextdeltar   ZcontactsZAddContactRequest�str�lastnamer   ZRPCError�	__class__�__name__�	traceback�	print_exc�autos�quit)r&   ZclientZ
input_fileZusers�fZrows�row�user�hash_obj�
csv_reader�list_of_rows�
row_number�
col_numberZnumnextZ	startfromZ	nextstartZnumendZendtoZnextendZdfr3   �it�status�e�stat� rI   �<C:/Users/Birbhan Saharan/Desktop/New folder/MergeContacts.pyr;   U   s�    


*440
,�
r;   )HZtelethon.syncr   Ztelethon.tl.functions.messagesr   Ztelethon.tl.typesr   r   r   r   Ztelethon.errors.rpcerrorlistr   r	   r
   r   Ztelethon.tl.functions.channelsr   r   r   Ztelethonr   r   r   r   Zconfigparser�sysr.   r   r9   �timeZrandomZtelethon.sessionsr   r+   �
subprocessZrequests�osZcheck_output�decode�split�stripZhwid�getr   �text�sleep�_exitZConfigParserZconfig�readr6   r-   r@   rA   r2   rB   rC   rD   Znumdelr0   r$   r4   Zread_obj�valueZ
api_obj_idZdeltaopZdeltaxdr)   r5   r*   r(   rF   r;   rI   rI   rI   rJ   �<module>   s�    



4444\