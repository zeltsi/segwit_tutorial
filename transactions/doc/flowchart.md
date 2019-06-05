graph TD
A[nVersion]
B[Marker]
C[Flag]
D[ScriptCode]
E[Amount]
F[Tx_In_count]
G[Outpoint]
H[Sequence]
I[Redeem_Scrip]
J[Tx_Out_Count]
K[Output]
L[nLockTime]
M[Sighash]
N[Witness]
O[hashPrevouts]
P[hashSequence]
Q[hashOutputs]
R[FinalTx]
S[Bip143]
T[Private key]
U[Public Key]
V[HashedPubKey]

A --> S
A --> R
G -->|Hashed| O
O --> S
G --> S
G --> R
H -->|Hashed| P
P --> S
D --> S
E --> S
H --> S 
H --> R
K -->|Hashed| Q
Q --> S
K --> R
L --> S
L --> R
M --> S
B --> R
C --> R
F --> R
I --> R
J --> R
S -->|Signing| N
N --> R
T --> U
U --> N
U --> V
V --> D
V --> I


https://mermaidjs.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbkFbblZlcnNpb25dXG5CW01hcmtlcl1cbkNbRmxhZ11cbkRbU2NyaXB0Q29kZV1cbkVbQW1vdW50XVxuRltUeF9Jbl9jb3VudF1cbkdbT3V0cG9pbnRdXG5IW1NlcXVlbmNlXVxuSVtSZWRlZW1fU2NyaXBdXG5KW1R4X091dF1cbktbT3V0cHV0XVxuTFtuTG9ja1RpbWVdXG5NW1NpZ2hhc2hdXG5OW1dpdG5lc3NdXG5PW2hhc2hQcmV2b3V0c11cblBbaGFzaFNlcXVlbmNlXVxuUVtoYXNoT3V0cHV0c11cblJbRmluYWxUeF1cblNbQmlwMTQzXVxuXG5BIC0tPiBTXG5BIC0tPiBSXG5HIC0tPnxIYXNoZWR8IE9cbk8gLS0-IFNcbkcgLS0-IFNcbkcgLS0-IFJcbkggLS0-fEhhc2hlZHwgUFxuUCAtLT4gU1xuRCAtLT4gU1xuRSAtLT4gU1xuSCAtLT4gUyBcbksgLS0-fEhhc2hlZHwgUVxuUSAtLT4gU1xuSyAtLT4gUlxuTCAtLT4gU1xuTCAtLT4gUlxuTSAtLT4gU1xuQiAtLT4gUlxuQyAtLT4gUlxuRiAtLT4gUlxuSSAtLT4gUlxuSiAtLT4gUlxuTiAtLT4gUlxuUyAtLT58U2lnbmVkIFdpdG5lc3N8IFIiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9fQ