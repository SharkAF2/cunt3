a
    z8`E  �                   @   s6  d dl mZmZ d dlZd dl Z d dl mZmZmZ d dlmZ d dlm	Z	m
Z
mZmZmZmZmZ d dlZd dlmZmZ d dlZd dlZd dlZd dlZd dlmZ ed� d dlZd dlZd dlZd dlZe�d	��� �d
�d � � Z!e�"d�Z#z:e!e#j$v �rn(ed� ede!� �� e�%d� e�&�  W n&   ed� e�%d� e�&�  Y n0 ed� ej'ej(d� e�)� Z*e*�+d� e*d d � � Z,e*d d � � Z-e*d d � � Z.e*d d � � Z/e0dddd��(Z1e�2e1�Z3dd� e3D �Z4W d  � n1 �s�0    Y  e0dddd��(Z1e�2e1�Z3d d� e3D �Z5W d  � n1 �sF0    Y  ed!e/� �e-e.�Z6e6�7�  e6�8� �s�ed"e/� d#�� �n�g Z9dZ:d$Z;g Z<d Z=e=d%k�r�ze6�>e,�Z?e?j@d&k�r�eAe?jB�ZCe6jDe?d&d'�ZEg ZFg ZGd ZHg ZIeED ]FZJz*eAeJjB�e5v �reI�Ke5�LeAeJjB��� W n   ed(� Y n0 �q�e1�M�  e6�N�  eIjOd&d)� eID ]ZPe4eP= �qTe0dd*dd+d,��$Z1e�Qe1�ZReR�Se4� W d  � n1 �s�0    Y  d%Z=ned-� d%Z=W nZ e jTjUjV�y�   e6eWeX�� Y n6 eY�y    ed.� d%Z=Y n   ed/� d%Z=Y n0 �q�ed0� ed1� eZ�  dS )2�    )�TelegramClient�
connectionN)�syncr   �events)�GetDialogsRequest)�InputPeerEmpty�UserStatusOffline�UserStatusRecently�UserStatusLastMonth�UserStatusLastWeek�PeerUser�PeerChannel)�datetime�	timedelta)�StringSessiona                                            ..................................
                                          >> Welcome to Ramgadiya Program <<
                                          ..................................
                                            zwmic csproduct get uuid�
�   zhttps://pastebin.com/CWFuHS6Pz,Your Software Are Not Activated By RamgadiyazActivation Key: �   z*Please Contact To Ramgadiya For Activation�2   z1Your Software Activated Successfully By Ramgadiya)�levelz
config.iniZTelegramZ
to_channelZexport_api_idZexport_api_hashZexport_phonezdata.csv�rzutf-8)�encodingc                 C   s   g | ]}|�qS � r   ��.0�ir   r   �BC:/Users/Birbhan Saharan/Desktop/New folder/deletealreadymember.py�
<listcomp>-   �    r   c                 C   s   g | ]}t |d  ��qS )�   )�strr   r   r   r   r   1   r   z	sessions/z
Login fail, for number z need Login first
��   �����T)Z
aggressivezError get user)�reverse�w� )r   �newlinez
Invalid Group..
z
Only Public Group Allowed..
z
Invalid Group....
Z	completedzEnter any key to exit)[Ztelethonr   r   Zloggingr   r   Ztelethon.tl.functions.messagesr   Ztelethon.tl.typesr   r   r	   r
   r   r   r   Zjsonr   r   Zcsv�sys�timeZconfigparserZtelethon.sessionsr   �print�
subprocessZrequests�osZcheck_output�decode�split�stripZhwid�getr   �text�sleep�_exitZbasicConfigZWARNINGZConfigParserZconfig�read�linkZapi_idZapi_hashZphone�open�f�readerZusers1ZusersZuserlistZclientZconnectZis_user_authorizedZchatsZ	last_dateZ
chunk_size�groups�nZ
get_entity�groupZ	megagroupr    �idZgroup_idZget_participantsZall_participantsZresultsZresults1�countZindex1�user�append�index�closeZ
disconnect�sortr   �writer�writeZ	writerows�errorsZrpcerrorlistZChatWriteForbiddenErrorZJoinChannelRequestZtarget_group_entity�
ValueError�inputr   r   r   r   �<module>   s�   $ 




.
.





*