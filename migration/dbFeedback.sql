create database dbFeedback;

use dbFeedback;

create table tbComentario (
    cod_comentario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    comentario TEXT NOT NULL,
    data_comentario DATETIME NOT NULL
);

