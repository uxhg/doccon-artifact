from typing import NamedTuple

from datalog.dlexpr import Expr
from datalog.newtypes import ContractName, FunctionName, Event, Param, FnMod


class HasFnFact(NamedTuple):
    ct: ContractName
    fn: FunctionName

    def __str__(self):
        return f"{self.ct}\t{self.fn}"


class HasParamFact(NamedTuple):
    ct: ContractName
    fn: FunctionName
    p: Param

    def __str__(self):
        return f"{self.ct}\t{self.fn}\t{self.p}"


class SeeFnFact(NamedTuple):
    cur_ct: ContractName
    cur_fn: FunctionName
    target_ct: ContractName
    target_fn: FunctionName

    def __str__(self):
        return f"{self.cur_ct}\t{self.cur_fn}\t{self.target_ct}\t{self.target_fn}"


class RequireFact(NamedTuple):
    ct: ContractName
    fn: FunctionName
    condition: Expr

    def __str__(self):
        return f"{self.ct}\t{self.fn}\t{self.condition}"


class EmitFact(NamedTuple):
    ct: ContractName
    fn: FunctionName
    event: Event
    condition: Expr

    def __str__(self):
        return f"{self.ct}\t{self.fn}\t{self.event}\t{self.condition}"


class RevertFact(NamedTuple):
    ct: ContractName
    fn: FunctionName
    condition: Expr

    def __str__(self):
        return f"{self.ct}\t{self.fn}\t{self.condition}"


class FnModFact(NamedTuple):
    """
    Write facts to "FnHasMod.facts"
    """
    ct: ContractName
    fn: FunctionName
    mod: FnMod

    def __str__(self):
        return f"{self.ct}\t{self.fn}\t{self.mod}"


class OverrideFact(NamedTuple):
    """
    Write facts to "Override.facts"
    """
    parent_ct: ContractName
    parent_fn: FunctionName
    child_ct: ContractName
    child_fn: FunctionName

    def __str__(self):
        return f"{self.parent_ct}\t{self.parent_fn}\t{self.child_ct}\t{self.child_fn}"
