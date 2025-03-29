        rindex = 0
        for data in cur:
            cindex = 0
            for rdata in data:
                self.tableMaxValue.setItem(rindex, cindex, QtWidgets.QTableWidgetItem(str(rdata)))
                cindex += 1
            rindex += 1
