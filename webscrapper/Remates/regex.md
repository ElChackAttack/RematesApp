# Lista de Regex para limpiar la artesania de Costa Rica

### Encontrar # expediente
`expediente([^(.,;)]+)`

### Encontrar precio base primer remate
`con una base de ([^(,.)]+)[,|.]`

### Encontrar todo segundo remate
`segundo remate se efectuara([^)\)]+\))`

### Encontrar todo tercer remate
`tercer remate([^)\)]+\))`