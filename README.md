# Alles Cosmos Registry

## Directory

### Assets

This folder contains assets (images, logos, etc.) for projects, tokens, addresses and other items.

### Chains

This folder contains information on items on each of the supported chains. For each chain, the following information are available

#### Project

```ts
type Social = {
    name: string;
    url: string;
}

type Code = {
    name: string;
    id: string;
}

type Contract = {
    name: stirng;
    address: string;
}

type Project = {
    name: string;
    website: string;
    github: string;
    logo: string;
    socials: Social[];
    codes: Code[];
    contracts: Contract[];
} 
```