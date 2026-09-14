const express = require ('express') ;
const app = express() ;
const port = 3000 ;

app.get('/', (req, res) => {
    res.send('aplicaçao rodando em container docker!');
});
app.listen(port, ()=> {
    console.log('servidor rodando na porta ${port}');
});