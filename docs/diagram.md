```mermaid
graph erDiagram;
    ITEM {
        string id
        int peso
        float ml
        string cor
        dateFormat criacao
    };
    COMPRADOR {
        string id
        bool sexo
        dateFormat nascimento
        dateFormat criacao
    };
    VENDEDOR {
        string id
        string endereco
        dateFormat criacao
    };
    PRODUTO {
        string id_VENDEDOR
        string id_ITEM
        int PRECO
        dateFormat compra_data
    };
    COMPRADOR ||--o{ COMPRA : faz;
    VENDEDOR ||--o{ PRODUTO : possui;
    COMPRA ||--o{ PRODUTO : tem;
    ITEM ||--o{ PRODUTO : possui;
```
