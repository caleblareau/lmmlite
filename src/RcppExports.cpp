// This file was generated by Rcpp::compileAttributes
// Generator token: 10BE3573-1514-4C36-9D1C-5A225CD40393

#include <RcppEigen.h>
#include <Rcpp.h>

using namespace Rcpp;

// R_calc_xpx
NumericMatrix R_calc_xpx(const NumericMatrix& X);
RcppExport SEXP lmmlite_R_calc_xpx(SEXP XSEXP) {
BEGIN_RCPP
    Rcpp::RObject __result;
    Rcpp::RNGScope __rngScope;
    Rcpp::traits::input_parameter< const NumericMatrix& >::type X(XSEXP);
    __result = Rcpp::wrap(R_calc_xpx(X));
    return __result;
END_RCPP
}
// R_eigen_decomp
List R_eigen_decomp(NumericMatrix A);
RcppExport SEXP lmmlite_R_eigen_decomp(SEXP ASEXP) {
BEGIN_RCPP
    Rcpp::RObject __result;
    Rcpp::RNGScope __rngScope;
    Rcpp::traits::input_parameter< NumericMatrix >::type A(ASEXP);
    __result = Rcpp::wrap(R_eigen_decomp(A));
    return __result;
END_RCPP
}