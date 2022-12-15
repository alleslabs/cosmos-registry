# Alles Cosmos Registry

## Entities

Entities list in [data/entities.json](data/entities.json) is the main list of all of the labelled actors (projects, protocols, individuals) that the registry is aware of. Each entity has a corresponding `slug` that is used as the reference key for all of its related data points and information (accounts, codes, contracts, etc).

```ts
type Social = {
    // The name of the social media
    name: string,
    // The corresponding link to the entity's social media page
    url: string,
}

type Entity = {
    // The slug identifier for the entity
    slug: string,
    // The human-readable name of the entity
    name: string,
    // The entity's main website
    website: string,
    // The entity's GitHub organization/account slug
    github: string,
    // The filename of the entity's logo located in assets/entities
    logo: string,
    // The list of the entity's supported social media info
    socials: Social[3]
}
```

### Codes

```ts
type Code = {
    // The slug identifier for the owner entity
    slug: string
    // The name describing the code
    name: string
    // The ID of the code on-chain
    id: string
}
```

### Contracts

```ts
type Contract = {
    // The slug identifier for the owner entity
    slug: string
    // The short description of the smart contract
    name: string
    // The address of the smart contract
    address: string
}
```

### Accounts

```ts
type Account = {
    // The slug identifier for the owner entity
    slug: string
    // The short description of the account
    name: string
    // The address of the account
    address: string
}
```

### Projects

```ts
type Project = {
    // The slug identifier for the owner project
    slug: string,
    // The list of contracts belonging to the project
    contracts: Contract[]
    // The list of codes belonging to the project
    codes : Code[]
    // The list of accounts belonging to the project
    accounts: Account[]
}
```

