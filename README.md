# DocCon_Artifact

[![DOI](https://zenodo.org/badge/521190909.svg)](https://zenodo.org/badge/latestdoi/521190909)


We apply for the **Available** and **Reusable** badges for this artifact submission.

The latest version of this repo can be found at: https://github.com/uxhg/doccon-artifact

DocCon is a tool for detecting inconsistency errors between documentations and the corresponding code for
Solidity smart contract libraries.


## Prerequisites
+ Linux OS (tested on Debian/sid, Ubuntu/16.04)
+ Docker (tested with 20.10.14, should work on newer versions)
+ At least 3GB space for the docker image

## Installation
Clone this repo and build Docker image:
```sh
git clone https://github.com/uxhg/doccon-artifact.git
cd doccon-artifact
sudo docker build -t doccon .
```

Time estimation: 20–30 minutes (on modern hardware with good network condition)

If successful, at the end of the command line output should look similar to the following:
```sh
Successfully built 778036834c4e 
Successfully tagged doccon:latest 
```

## Run and Interprete the Results
After building the Docker image, you can start the Docker container:

```sh
sudo docker run --name doccon --rm -it doccon
```
Once started, the container will start the end-to-end evaluation process automatically, which consists of three parts.
+ Code facts extraction
+ Documentation facts extraction
+ Inconsistency error detection

The process may take about three minutes. You will see many text lines printing on the screen. 
The following banner indicates the beginning of the presented results
(note: better viewed in a window with at least 100 columns wide).
```sh
##############################################################
#                  Results Starts Here                       #
##############################################################
```

### Subjects
All the detected API documentation inconsistency errors are from the following three popular smart contract libraries.
+ [OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts)
+ [ERC721-Extensions](https://github.com/1001-digital/erc721-extensions/)
+ [Dappsys](https://github.com/dapphub/dappsys)


### Results

Here we list all the reported bugs (documentation-code inconsistency errors), grouped by the original issues we created to report them.
Different issue reports are separated by dashed ines.
Each issue may contain more than one inconsistency errors. 

For each issue, we list the URL, the number of inconsistencies, the inconsistent facts, and its file locations (note: we use Datalog facts to
represent documentation and code, and compute their differences). 
It is also shown whether each issue has been confirmed or fixed.

In total, there are 19 issues, containing 40 inconsistency errors.

```
All Reported Cases
==================================================================================
Reported issue 1: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3359
Contain 2 inconsistencies    Confirmed Fixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasParam.csv:ERC20 _transfer       recipient
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasParam.csv:ERC20 _transfer       sender
----------------------------------------------------------------------------------
Reported issue 2: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3360
Contain 2 inconsistencies    Confirmed Fixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasParam.csv:ERC777        _mint   data
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasParam.csv:ERC777        _mint   operator
----------------------------------------------------------------------------------
Reported issue 3: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3361
Contain 2 inconsistencies    NotConfirmed NotFixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasParam.csv:IERC777       send    operatorData
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasParam.csv:IERC777       burn    operatorData
----------------------------------------------------------------------------------
Reported issue 4: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3362
Contain 3 inconsistencies    Confirmed NotFixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1Require.csv:ERC721 safeTransferFrom        $Cmp($Literal(from), $Literal(address(0)), NEQ)
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1Require.csv:ERC721 transferFrom    $Cmp($Literal(from), $Literal(address(0)), NEQ)
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1Require.csv:ERC721 _safeTransfer   $Cmp($Literal(from), $Literal(address(0)), NEQ)
----------------------------------------------------------------------------------
Reported issue 5: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3363
Contain 1 inconsistencies    Confirmed Fixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasParam.csv:ERC721        _safeMint       data
----------------------------------------------------------------------------------
Reported issue 6: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3366
Contain 4 inconsistencies    Confirmed NotFixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1Require.csv:EnumerableMap  _at     $Cmp($Literal(index), $Literal({length}), LT)
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1Require.csv:EnumerableMap  at      $Cmp($Literal(index), $Literal({length}), LT)
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1Require.csv:EnumerableSet  _at     $Cmp($Literal(index), $Literal({length}), LT)
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1Require.csv:EnumerableSet  at      $Cmp($Literal(index), $Literal({length}), LT)
----------------------------------------------------------------------------------
Reported issue 7: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3367
Contain 4 inconsistencies    Confirmed Fixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasParam.csv:ERC1155       _beforeTokenTransfer    amount
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasParam.csv:ERC1155       _beforeTokenTransfer    id
----------------------------------------------------------------------------------
Reported issue 8: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3368
Contain 2 inconsistencies    Confirmed Fixed
(The 2 inconsistencies involves overloaded methods, thus only 1 fact here)
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1Emit.csv:VestingWallet     release TokensReleased  $Bool(True)
----------------------------------------------------------------------------------
Reported issue 9: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3369
Contain 3 inconsistencies    Confirmed Fixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L2Emit.csv:Escrow    deposit Deposited       $Bool(True)
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L2Emit.csv:Escrow    withdraw        Withdrawn       $Bool(True)
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L2Emit.csv:PullPayment       _asyncTransfer  Deposited       $Bool(True)
----------------------------------------------------------------------------------
Reported issue 10: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3376
Contain 1 inconsistency    Confirmed Fixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L2Emit.csv:AccessControl     _grantRole      RoleGranted     $Bool(True)
----------------------------------------------------------------------------------
Reported issue 11: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3377
Contain 1 inconsistency    Confirmed Fixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasFn.csv:ERC3156FlashBorrower     onFlashLoan
----------------------------------------------------------------------------------
Reported issue 12: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3374
Contain 1 inconsistency    Confirmed Fixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L2Emit.csv:ERC1155   _mintBatch      TransferBatch   $Bool(True)
----------------------------------------------------------------------------------
Reported issue 13: https://github.com/OpenZeppelin/openzeppelin-contracts/issues/3378
Contain 2 inconsistencies    NotConfirmed NotFixed
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasParam.csv:IERC1820Registry      setInterfaceImplementer interfaceHash
/opt/doccon/exp/dl/out/openzeppelin/v4.5.0/L1HasParam.csv:IERC1820Registry      getInterfaceImplementer interfaceHash
----------------------------------------------------------------------------------
Reported issue 14: https://github.com/1001-digital/erc721-extensions/issues/12
Contain 2 inconsistencies    Confirmed Fixed
/opt/doccon/exp/dl/out/erc721-extensions/v0.0.18/L1Override.csv:HasSecondarySalesFees   getFeeRecipients        WithFees        getFeeRecipients
/opt/doccon/exp/dl/out/erc721-extensions/v0.0.18/L1Override.csv:HasSecondarySalesFees   getFeeBps       WithFees        getFeeBps
----------------------------------------------------------------------------------
Reported issue 15: https://github.com/1001-digital/erc721-extensions/issues/13
Contain 5 inconsistencies    NotConfirmed NotFixed
/opt/doccon/exp/dl/out/erc721-extensions/v0.0.18/L2Emit.csv:WithMarketOffers    _cancelOffer    OfferWithdrawn  $Bool(True)
/opt/doccon/exp/dl/out/erc721-extensions/v0.0.18/L2Emit.csv:WithMarketOffers    _beforeTokenTransfer    OfferWithdrawn  $Bool(True)
/opt/doccon/exp/dl/out/erc721-extensions/v0.0.18/L2Emit.csv:WithMarketOffers    cancelOffer     OfferWithdrawn  $Bool(True)
/opt/doccon/exp/dl/out/erc721-extensions/v0.0.18/L2Emit.csv:WithMarketOffers    _makeOffer      OfferCreated    $Bool(True)
/opt/doccon/exp/dl/out/erc721-extensions/v0.0.18/L2Emit.csv:WithMarketOffers    makeOfferTo     OfferCreated    $Bool(True)
----------------------------------------------------------------------------------
Reported issue 16: https://github.com/dapphub/ds-chief/issues/14
Contain 2 inconsistencies    NotConfirmed NotFixed
/opt/doccon/exp/dl/out/dapphub/ds-chief/L1Emit.csv:DSChiefApprovals     lock    LogLockFree     $Bool(True)
/opt/doccon/exp/dl/out/dapphub/ds-chief/L1Emit.csv:DSChiefApprovals     free    LogLockFree     $Bool(True)
----------------------------------------------------------------------------------
Reported issue 17: https://github.com/dapphub/ds-chief/issues/16
Contain 2 inconsistencies    NotConfirmed NotFixed
/opt/doccon/exp/dl/out/dapphub/ds-chief/L2Emit.csv:DSChiefApprovals     vote    Etch    $Bool(True)
/opt/doccon/exp/dl/out/dapphub/ds-chief/L2Emit.csv:DSChiefApprovals     etch    Etch    $Bool(True)
----------------------------------------------------------------------------------
Reported issue 18: https://github.com/dapphub/ds-auth/issues/14
Contain 1 inconsistency    NotConfirmed NotFixed
/opt/doccon/exp/dl/out/dapphub/ds-auth/L2Emit.csv:DSAuth        setOwner        LogSetOwner     $Bool(True)
----------------------------------------------------------------------------------
Reported issue 19: https://github.com/dapphub/ds-token/issues/39
Contain 2 inconsistencies    NotConfirmed NotFixed
/opt/doccon/exp/dl/out/dapphub/ds-token/L2Emit.csv:DSToken      transferFrom    Transfer        $Bool(True)
/opt/doccon/exp/dl/out/dapphub/ds-token/L2Emit.csv:DSToken      transfer        Transfer        $Bool(True)
==================================================================================
In total: 40 reported inconsistencies, 25 level-1, 15 level-2, 24 confirmed, 17 fixed.
```

After our paper submission, developers confirmed and fixed [another
issue (issue 15 above)](https://github.com/1001-digital/erc721-extensions/issues/13) containing 5 inconsistencies,
increasing the confirmation rate to (24+5)/40 = 72.5%.

This issue led developers to [discover that they had redundant event
emission](https://github.com/1001-digital/erc721-extensions/issues/16) in their code. By removing
the unnecessary event emission, they can reduce gas cost of the contract, thus brings real-world
economic value.


## More Details

### All Detected Errors
We report the total level-1/2/3 numbers of detected errors in the Table.4 of the paper. 
Those numbers can be verified by counting the numbers of lines of those files as below. 
You can also inspect those files to see the corresponding facts.
```
root@a720f1dd5aef:/opt/doccon# wc -l /opt/doccon/exp/dl/out/openzeppelin/v4.5.0/all-L*.csv
    47 /opt/doccon/exp/dl/out/openzeppelin/v4.5.0/all-L1.csv
   567 /opt/doccon/exp/dl/out/openzeppelin/v4.5.0/all-L2.csv
  3742 /opt/doccon/exp/dl/out/openzeppelin/v4.5.0/all-L3.csv

root@a720f1dd5aef:/opt/doccon# sort -u /opt/doccon/exp/dl/out/dapphub/l1-total.csv | wc -l
4
root@a720f1dd5aef:/opt/doccon# sort -u /opt/doccon/exp/dl/out/dapphub/l2-total.csv | wc -l
163
root@a720f1dd5aef:/opt/doccon# sort -u /opt/doccon/exp/dl/out/dapphub/l3-total.csv | wc -l
655

root@a720f1dd5aef:/opt/doccon# wc -l /opt/doccon/exp/dl/out/erc721-extensions/v0.0.18/all-L*.csv
    2 /opt/doccon/exp/dl/out/erc721-extensions/v0.0.18/all-L1.csv
   79 /opt/doccon/exp/dl/out/erc721-extensions/v0.0.18/all-L2.csv
  377 /opt/doccon/exp/dl/out/erc721-extensions/v0.0.18/all-L3.csv
```


### Files and Directories
Inside docker everything we used resides inside `/opt/doccon`.

You can inspect: 
+ `Code2Schema`, `smart_factbase`: the extractors we build to extract facts.
+ `datalog`: Datalog rules we used to query.
+ `exp/dl/in`: facts generated by extractors.
+ `exp/dl/out`: queried results, all our results above can be found in files under it.

```
├──📂 Code2Schema        # code facts extractor
├──📂 smart_factbase     # doc facts extractor
├──📂 datalog            # datalog definitions, inference rules
├──📂 library-src        # source of generated 
├──📂 library-facts      # generated code facts, will be linked to exp/dl/in dir
├──📂 exp                # storing generated data and pre-installed data
|  ├─📂 dl               # datalog related
|  | ├─📂  in            # inference input, will link to generated codefacts and docfacts
|  | └─📂  out           # inference output
|  └─📂doc_facts         # generated doc facts, will be linked to exp/dl/in dir
|     ├─📂  dapphub
|     ├─📂  erc721-extensions
|     └─📂  openzeppelin
└──📄 entry.sh           # bash script which automatically run after the container starts
```
