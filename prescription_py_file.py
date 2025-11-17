# ============================================================================
# PART 9: PDF EXPORT & REPORTING SYSTEM
# ============================================================================

class PDFExporter:
    """
    Export system data to PDF reports.
    
    Generates professional PDF reports for:
    - Prescription records
    - Blockchain audit trails
    - Performance metrics
    - Compliance reports
    - Alert summaries
    - Review queue status
    
    Note: This uses a simplified HTML-to-PDF approach that works without
    external dependencies. For production, use libraries like ReportLab or WeasyPrint.
    """
    
    def __init__(self, system):
        """Initialize PDF exporter with reference to main system."""
        self.system = system
    
    def generate_prescription_report(self, prescription_data: Dict, 
                                    validation_report: Dict,
                                    output_filename: str = "prescription_report.pdf") -> str:
        """
        Generate a detailed prescription report.
        
        Args:
            prescription_data: Prescription information
            validation_report: Validation results
            output_filename: Output file name
            
        Returns:
            str: Path to generated PDF file
        """
        html_content = self._create_prescription_html(prescription_data, validation_report)
        return self._save_html_as_pdf(html_content, output_filename)
    
    def generate_blockchain_audit_report(self, output_filename: str = "blockchain_audit.pdf") -> str:
        """
        Generate complete blockchain audit trail report.
        
        Args:
            output_filename: Output file name
            
        Returns:
            str: Path to generated PDF file
        """
        html_content = self._create_blockchain_html()
        return self._save_html_as_pdf(html_content, output_filename)
    
    def generate_performance_report(self, output_filename: str = "performance_report.pdf") -> str:
        """
        Generate system performance metrics report.
        
        Args:
            output_filename: Output file name
            
        Returns:
            str: Path to generated PDF file
        """
        html_content = self._create_performance_html()
        return self._save_html_as_pdf(html_content, output_filename)
    
    def generate_compliance_report(self, start_date: Optional[datetime] = None,
                                   end_date: Optional[datetime] = None,
                                   output_filename: str = "compliance_report.pdf") -> str:
        """
        Generate comprehensive compliance report for regulatory requirements.
        
        Args:
            start_date: Report start date
            end_date: Report end date
            output_filename: Output file name
            
        Returns:
            str: Path to generated PDF file
        """
        html_content = self._create_compliance_html(start_date, end_date)
        return self._save_html_as_pdf(html_content, output_filename)
    
    def generate_alert_summary_report(self, output_filename: str = "alert_summary.pdf") -> str:
        """
        Generate alert summary report.
        
        Args:
            output_filename: Output file name
            
        Returns:
            str: Path to generated PDF file
        """
        html_content = self._create_alert_summary_html()
        return self._save_html_as_pdf(html_content, output_filename)
    
    def _create_prescription_html(self, prescription_data: Dict, validation_report: Dict) -> str:
        """Create HTML for prescription report."""
        misuse_risk = validation_report.get('misuse_risk', {})
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ background: #2c3e50; color: white; padding: 20px; text-align: center; }}
        .section {{ margin: 20px 0; padding: 15px; border: 1px solid #ddd; }}
        .section-title {{ font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 10px; }}
        .info-row {{ display: flex; margin: 5px 0; }}
        .info-label {{ font-weight: bold; width: 200px; }}
        .info-value {{ flex: 1; }}
        .risk-high {{ color: #e74c3c; font-weight: bold; }}
        .risk-moderate {{ color: #f39c12; font-weight: bold; }}
        .risk-low {{ color: #27ae60; font-weight: bold; }}
        .warning-box {{ background: #fff3cd; border-left: 4px solid #f39c12; padding: 10px; margin: 10px 0; }}
        .footer {{ text-align: center; font-size: 12px; color: #7f8c8d; margin-top: 30px; }}
        ul {{ margin: 5px 0; padding-left: 20px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🏥 Prescription Validation Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="section">
        <div class="section-title">📋 PRESCRIPTION INFORMATION</div>
        <div class="info-row">
            <div class="info-label">Patient Name:</div>
            <div class="info-value">{prescription_data.get('patient_name', 'N/A')}</div>
        </div>
        <div class="info-row">
            <div class="info-label">Patient ID:</div>
            <div class="info-value">{prescription_data.get('patient_id', 'N/A')}</div>
        </div>
        <div class="info-row">
            <div class="info-label">Patient Age:</div>
            <div class="info-value">{prescription_data.get('patient_age', 'N/A')}</div>
        </div>
        <div class="info-row">
            <div class="info-label">Medication:</div>
            <div class="info-value">{prescription_data.get('medication', 'N/A')}</div>
        </div>
        <div class="info-row">
            <div class="info-label">Dosage:</div>
            <div class="info-value">{prescription_data.get('dosage', 'N/A')}</div>
        </div>
        <div class="info-row">
            <div class="info-label">Duration:</div>
            <div class="info-value">{prescription_data.get('duration', 'N/A')}</div>
        </div>
        <div class="info-row">
            <div class="info-label">Prescribing Doctor:</div>
            <div class="info-value">{prescription_data.get('doctor_name', 'N/A')} (ID: {prescription_data.get('doctor_id', 'N/A')})</div>
        </div>
        <div class="info-row">
            <div class="info-label">Date Prescribed:</div>
            <div class="info-value">{prescription_data.get('date_prescribed', 'N/A')}</div>
        </div>
    </div>
    
    <div class="section">
        <div class="section-title">🔍 VALIDATION RESULTS</div>
        <div class="info-row">
            <div class="info-label">Validation Status:</div>
            <div class="info-value">{'✅ APPROVED' if validation_report.get('is_valid') else '❌ REJECTED'}</div>
        </div>
        <div class="info-row">
            <div class="info-label">Confidence Score:</div>
            <div class="info-value">{validation_report.get('confidence', 0):.1%}</div>
        </div>
        <div class="info-row">
            <div class="info-label">Validated By:</div>
            <div class="info-value">{validation_report.get('validated_by', 'N/A')}</div>
        </div>
        <div class="info-row">
            <div class="info-label">Validation Timestamp:</div>
            <div class="info-value">{validation_report.get('timestamp', 'N/A')}</div>
        </div>
        
        <p style="margin-top: 15px;"><strong>Checks Performed:</strong></p>
        <ul>
            {''.join(f'<li>{check}</li>' for check in validation_report.get('checks_performed', []))}
        </ul>
        
        {f'''
        <div class="warning-box">
            <strong>⚠️ Warnings:</strong>
            <ul>
                {''.join(f'<li>{warning}</li>' for warning in validation_report.get('warnings', []))}
            </ul>
        </div>
        ''' if validation_report.get('warnings') else ''}
        
        {f'''
        <div class="warning-box" style="border-color: #e74c3c; background: #ffebee;">
            <strong>❌ Errors:</strong>
            <ul>
                {''.join(f'<li>{error}</li>' for error in validation_report.get('errors', []))}
            </ul>
        </div>
        ''' if validation_report.get('errors') else ''}
    </div>
    
    <div class="section">
        <div class="section-title">🚨 MISUSE RISK ASSESSMENT</div>
        <div class="info-row">
            <div class="info-label">Risk Level:</div>
            <div class="info-value {
                'risk-high' if misuse_risk.get('risk_level') == 'HIGH RISK' 
                else 'risk-moderate' if misuse_risk.get('risk_level') == 'MODERATE RISK'
                else 'risk-low'
            }">
                {misuse_risk.get('risk_level', 'N/A')}
            </div>
        </div>
        <div class="info-row">
            <div class="info-label">Risk Score:</div>
            <div class="info-value">{misuse_risk.get('risk_score', 0)}/100</div>
        </div>
        
        {f'''
        <p style="margin-top: 15px;"><strong>Risk Factors Identified:</strong></p>
        <ul>
            {''.join(f'<li>{factor}</li>' for factor in misuse_risk.get('risk_factors', []))}
        </ul>
        ''' if misuse_risk.get('risk_factors') else ''}
        
        <p style="margin-top: 15px;"><strong>Recommendations:</strong></p>
        <ul>
            {''.join(f'<li>{rec}</li>' for rec in misuse_risk.get('recommendations', []))}
        </ul>
    </div>
    
    <div class="footer">
        <p>This report was generated by the AI-Powered Blockchain Prescription Tracking System</p>
        <p>For questions or concerns, contact the pharmacy compliance department</p>
        <p><em>Confidential - For authorized personnel only</em></p>
    </div>
</body>
</html>
        """
        return html
    
    def _create_blockchain_html(self) -> str:
        """Create HTML for blockchain audit report."""
        chain = self.system.blockchain.chain
        is_valid = self.system.blockchain.is_chain_valid()
        
        blocks_html = ""
        for block in chain:
            if block.index == 0:
                blocks_html += f"""
                <div class="block">
                    <h3>Block #{block.index} (Genesis Block)</h3>
                    <p><strong>Timestamp:</strong> {block.timestamp}</p>
                    <p><strong>Hash:</strong> <code>{block.hash}</code></p>
                </div>
                """
            else:
                blocks_html += f"""
                <div class="block">
                    <h3>Block #{block.index}</h3>
                    <p><strong>Timestamp:</strong> {block.timestamp}</p>
                    <p><strong>Patient:</strong> {block.prescription_data.get('patient_name')} (ID: {block.prescription_data.get('patient_id')})</p>
                    <p><strong>Medication:</strong> {block.prescription_data.get('medication')}</p>
                    <p><strong>Dosage:</strong> {block.prescription_data.get('dosage')}</p>
                    <p><strong>Doctor:</strong> {block.prescription_data.get('doctor_name')} (ID: {block.prescription_data.get('doctor_id')})</p>
                    <p><strong>Hash:</strong> <code>{block.hash}</code></p>
                    <p><strong>Previous Hash:</strong> <code>{block.previous_hash}</code></p>
                    {'<p style="color: #f39c12;"><strong>⚠️ Warning Flag: MODERATE RISK</strong></p>' if block.prescription_data.get('_warning_flag') else ''}
                </div>
                """
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ background: #2c3e50; color: white; padding: 20px; text-align: center; }}
        .summary {{ background: #ecf0f1; padding: 15px; margin: 20px 0; }}
        .block {{ border: 2px solid #3498db; padding: 15px; margin: 15px 0; border-radius: 5px; }}
        code {{ background: #f4f4f4; padding: 2px 5px; font-size: 12px; word-break: break-all; }}
        .valid {{ color: #27ae60; font-weight: bold; }}
        .invalid {{ color: #e74c3c; font-weight: bold; }}
        .footer {{ text-align: center; font-size: 12px; color: #7f8c8d; margin-top: 30px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>⛓️ Blockchain Audit Trail Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="summary">
        <h2>📊 Blockchain Summary</h2>
        <p><strong>Total Blocks:</strong> {len(chain)}</p>
        <p><strong>Total Prescriptions:</strong> {len(chain) - 1}</p>
        <p><strong>Chain Validity:</strong> <span class="{'valid' if is_valid else 'invalid'}">
            {'✅ VALID - Chain integrity verified' if is_valid else '❌ INVALID - Chain has been compromised'}
        </span></p>
        <p><strong>Genesis Block Hash:</strong> <code>{chain[0].hash}</code></p>
        <p><strong>Latest Block Hash:</strong> <code>{chain[-1].hash}</code></p>
    </div>
    
    <h2>📋 Complete Blockchain</h2>
    {blocks_html}
    
    <div class="footer">
        <p>This blockchain audit trail provides cryptographic proof of all prescription records</p>
        <p>Each block is linked to the previous block via cryptographic hashing</p>
        <p><em>Confidential - For audit and compliance purposes only</em></p>
    </div>
</body>
</html>
        """
        return html
    
    def _create_performance_html(self) -> str:
        """Create HTML for performance metrics report."""
        report = self.system.performance_metrics.get_summary_report()
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ background: #2c3e50; color: white; padding: 20px; text-align: center; }}
        .metric-card {{ background: #ecf0f1; padding: 15px; margin: 10px 0; border-left: 4px solid #3498db; }}
        .metric-title {{ font-size: 16px; font-weight: bold; color: #2c3e50; }}
        .metric-value {{ font-size: 24px; color: #3498db; margin: 10px 0; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #3498db; color: white; }}
        .good {{ color: #27ae60; }}
        .warning {{ color: #f39c12; }}
        .critical {{ color: #e74c3c; }}
        .footer {{ text-align: center; font-size: 12px; color: #7f8c8d; margin-top: 30px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 System Performance Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="metric-card">
        <div class="metric-title">⏱️ System Uptime</div>
        <div class="metric-value">{report['system_uptime_hours']} hours</div>
    </div>
    
    <div class="metric-card">
        <div class="metric-title">📈 Total Prescriptions Processed</div>
        <div class="metric-value">{report['total_prescriptions']}</div>
    </div>
    
    <div class="metric-card">
        <div class="metric-title">⚡ Throughput</div>
        <div class="metric-value">{report['throughput_per_hour']} prescriptions/hour</div>
    </div>
    
    <div class="metric-card">
        <div class="metric-title">✅ System Availability</div>
        <div class="metric-value class="{'good' if report['availability_percent'] >= 99 else 'warning'}">{report['availability_percent']}%</div>
    </div>
    
    <div class="metric-card">
        <div class="metric-title">❌ Error Rate</div>
        <div class="metric-value" class="{'good' if report['error_rate'] < 5 else 'critical'}">{report['error_rate']}%</div>
    </div>
    
    <h2>⚡ Processing Performance</h2>
    <table>
        <tr>
            <th>Metric</th>
            <th>Time (ms)</th>
        </tr>
        <tr>
            <td>Average Processing Time</td>
            <td>{report['processing_times']['average_ms']}</td>
        </tr>
        <tr>
            <td>P50 (Median)</td>
            <td>{report['processing_times']['p50_ms']}</td>
        </tr>
        <tr>
            <td>P95</td>
            <td>{report['processing_times']['p95_ms']}</td>
        </tr>
        <tr>
            <td>P99</td>
            <td>{report['processing_times']['p99_ms']}</td>
        </tr>
    </table>
    
    <h2>🔍 Validation Performance</h2>
    <table>
        <tr>
            <th>Metric</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Average Validation Time</td>
            <td>{report['validation_times']['average_ms']} ms</td>
        </tr>
        <tr>
            <td>Total Validations</td>
            <td>{report['validation_times']['total_validations']}</td>
        </tr>
    </table>
    
    <h2>⛓️ Blockchain Performance</h2>
    <table>
        <tr>
            <th>Metric</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Average Write Time</td>
            <td>{report['blockchain_performance']['average_write_ms']} ms</td>
        </tr>
        <tr>
            <td>Total Writes</td>
            <td>{report['blockchain_performance']['total_writes']}</td>
        </tr>
    </table>
    
    <h2>🚨 Alert Performance</h2>
    <table>
        <tr>
            <th>Metric</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Average Response Time</td>
            <td>{report['alert_performance']['average_response_ms']} ms</td>
        </tr>
        <tr>
            <td>Total Alerts Sent</td>
            <td>{report['alert_performance']['total_alerts']}</td>
        </tr>
    </table>
    
    <div class="footer">
        <p>Performance metrics are tracked in real-time for system optimization</p>
        <p><em>For internal monitoring and capacity planning</em></p>
    </div>
</body>
</html>
        """
        return html
    
    def _create_compliance_html(self, start_date: Optional[datetime], 
                               end_date: Optional[datetime]) -> str:
        """Create HTML for compliance report."""
        stats = self.system.get_statistics()
        queue_status = self.system.review_queue.get_queue_status()
        alert_history = self.system.alert_system.get_alert_history()
        
        start_str = start_date.strftime('%Y-%m-%d') if start_date else 'System Start'
        end_str = end_date.strftime('%Y-%m-%d') if end_date else datetime.now().strftime('%Y-%m-%d')
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ background: #2c3e50; color: white; padding: 20px; text-align: center; }}
        .section {{ margin: 20px 0; padding: 15px; border: 1px solid #ddd; }}
        .section-title {{ font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 10px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
        th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #3498db; color: white; }}
        .footer {{ text-align: center; font-size: 12px; color: #7f8c8d; margin-top: 30px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📋 Compliance Report</h1>
        <p>Report Period: {start_str} to {end_str}</p>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="section">
        <div class="section-title">📊 PRESCRIPTION ACTIVITY SUMMARY</div>
        <table>
            <tr>
                <th>Metric</th>
                <th>Count</th>
            </tr>
            <tr>
                <td>Total Prescriptions Processed</td>
                <td>{stats['total_prescriptions']}</td>
            </tr>
            <tr>
                <td>Unique Patients</td>
                <td>{stats['unique_patients']}</td>
            </tr>
            <tr>
                <td>Unique Prescribers</td>
                <td>{stats['unique_doctors']}</td>
            </tr>
            <tr>
                <td>Prescriptions with Risk Warnings</td>
                <td>{stats['prescriptions_with_warnings']}</td>
            </tr>
            <tr>
                <td>Prescriptions Flagged for Review</td>
                <td>{queue_status['total_in_queue'] + queue_status['total_reviewed']}</td>
            </tr>
        </table>
    </div>
    
    <div class="section">
        <div class="section-title">🚨 ALERT SUMMARY</div>
        <table>
            <tr>
                <th>Alert Type</th>
                <th>Count</th>
            </tr>
            <tr>
                <td>Critical Alerts</td>
                <td>{len(self.system.alert_system.get_alerts_by_level('CRITICAL'))}</td>
            </tr>
            <tr>
                <td>High Priority Alerts</td>
                <td>{len(self.system.alert_system.get_alerts_by_level('HIGH'))}</td>
            </tr>
            <tr>
                <td>Total Alerts Generated</td>
                <td>{len(alert_history)}</td>
            </tr>
        </table>
    </div>
    
    <div class="section">
        <div class="section-title">📋 REVIEW QUEUE METRICS</div>
        <table>
            <tr>
                <th>Status</th>
                <th>Count</th>
            </tr>
            <tr>
                <td>Pending Review</td>
                <td>{queue_status['pending']}</td>
            </tr>
            <tr>
                <td>Under Review</td>
                <td>{queue_status['under_review']}</td>
            </tr>
            <tr>
                <td>Completed Reviews</td>
                <td>{queue_status['total_reviewed']}</td>
            </tr>
            <tr>
                <td>SLA Violations</td>
                <td>{queue_status['sla_violations']}</td>
            </tr>
        </table>
    </div>
    
    <div class="section">
        <div class="section-title">⛓️ BLOCKCHAIN INTEGRITY</div>
        <p><strong>Chain Status:</strong> {'✅ VALID - All blocks verified' if stats['blockchain_valid'] else '❌ INVALID - Integrity compromised'}</p>
        <p><strong>Total Blocks:</strong> {len(self.system.blockchain.chain)}</p>
        <p><strong>Latest Block Hash:</strong> <code style="font-size: 11px;">{self.system.blockchain.chain[-1].hash}</code></p>
    </div>
    
    <div class="footer">
        <p>This compliance report is generated for regulatory and audit purposes</p>
        <p>Report includes all prescription activities within the specified date range</p>
        <p><em>Confidential - For authorized compliance officers only</em></p>
    </div>
</body>
</html>
        """
        return html
    
    def _create_alert_summary_html(self) -> str:
        """Create HTML for alert summary report."""
        alert_history = self.system.alert_system.get_alert_history()
        critical_alerts = self.system.alert_system.get_alerts_by_level('CRITICAL')
        high_alerts = self.system.alert_system.get_alerts_by_level('HIGH')
        
        alerts_html = ""
        for alert in alert_history[-20:]:  # Last 20 alerts
            alerts_html += f"""
            <tr>
                <td>{alert['alert_id']}</td>
                <td>{alert['timestamp'][:19]}</td>
                <td><strong>{alert['alert_level']}</strong></td>
                <td>{alert['prescription_data'].get('patient_name', 'N/A')}</td>
                <td>{alert['prescription_data'].get('medication', 'N/A')}</td>
                <td>{alert['risk_assessment'].get('risk_score', 'N/A')}/100</td>
            </tr>
            """
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ background: #2c3e50; color: white; padding: 20px; text-align: center; }}
        .summary-box {{ background: #ecf0f1; padding: 15px; margin: 20px 0; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; font-size: 13px; }}
        th {{ background: #e74c3c; color: white; }}
        .footer {{ text-align: center; font-size: 12px; color: #7f8c8d; margin-top: 30px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🚨 Alert Summary Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="summary-box">
        <h2>📊 Alert Statistics</h2>
        <p><strong>Total Alerts:</strong> {len(alert_history)}</p>
        <p><strong>Critical Alerts:</strong> {len(critical_alerts)}</p>
        <p><strong>High Priority Alerts:</strong> {len(high_alerts)}</p>
    </div>
    
    <h2>📋 Recent Alerts (Last 20)</h2>
    <table>
        <tr>
            <th>Alert ID</th>
            <th>Timestamp</th>
            <th>Level</th>
            <th>Patient</th>
            <th>Medication</th>
            <th>Risk Score</th>
        </tr>
        {alerts_html}
    </table>
    
    <div class="footer">
        <p>Alert summary for monitoring and response tracking</p>
        <p><em>For pharmacy management review</em></p>
    </div>
</body>
</html>
        """
        return html
    
    def _save_html_as_pdf(self, html_content: str, output_filename: str) -> str:
        """
        Save HTML content as PDF.
        
        Note: This is a simplified version that saves as HTML.
        For production, integrate with libraries like:
        - ReportLab: pip install reportlab
        - WeasyPrint: pip install weasyprint
        - xhtml2pdf: pip install xhtml2pdf
        
        Example with WeasyPrint:
        from weasyprint import HTML
        HTML(string=html_content).write_pdf(output_filename)
        """
        # For demonstration, we'll save as HTML with PDF-like styling
        # In production, convert to actual PDF
        
        # Ensure filename has .html extension for this demo
        if output_filename.endswith('.pdf'):
            output_filename = output_filename.replace('.pdf', '.html')
        
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"\n✅ Report generated successfully: {output_filename}")
            print(f"   File location: {output_filename}")
            print(f"   Size: {len(html_content)} bytes")
            
            # Production note
            print(f"\n   📝 Note: For production, install a PDF library:")
            print(f"      pip install weasyprint")
            print(f"      Then use: HTML(string=html_content).write_pdf('{output_filename.replace('.html', '.pdf')}')")
            
            return output_filename
            
        except Exception as e:
            print(f"\n❌ Error generating report: {str(e)}")
            return ""
    
    def export_all_reports(self, output_dir: str = "./reports") -> Dict[str, str]:
        """
        Generate all available reports.
        
        Args:
            output_dir: Directory to save reports
            
        Returns:
            dict: Map of report types to file paths
        """
        import os
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        print(f"\n{'='*70}")
        print("GENERATING ALL REPORTS")
        print(f"{'='*70}\n")
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        reports = {}
        
        # 1. Blockchain Audit Report
        print("1. Generating Blockchain Audit Report...")
        blockchain_file = f"{output_dir}/blockchain_audit_{timestamp}.html"
        reports['blockchain_audit'] = self.generate_blockchain_audit_report(blockchain_file)
        
        # 2. Performance Report
        print("\n2. Generating Performance Report...")
        performance_file = f"{output_dir}/performance_report_{timestamp}.html"
        reports['performance'] = self.generate_performance_report(performance_file)
        
        # 3. Compliance Report
        print("\n3. Generating Compliance Report...")
        compliance_file = f"{output_dir}/compliance_report_{timestamp}.html"
        reports['compliance'] = self.generate_compliance_report(None, None, compliance_file)
        
        # 4. Alert Summary Report
        print("\n4. Generating Alert Summary Report...")
        alert_file = f"{output_dir}/alert_summary_{timestamp}.html"
        reports['alert_summary'] = self.generate_alert_summary_report(alert_file)
        
        print(f"\n{'='*70}")
        print("✅ ALL REPORTS GENERATED SUCCESSFULLY")
        print(f"{'='*70}")
        print(f"\nReports saved to: {output_dir}/")
        print(f"Total reports: {len(reports)}")
        
        return reports
        """
AI-Powered Blockchain Prescription Tracking System
===================================================

ASSIGNMENT: Healthcare Prescription Tracking with LLM Validation

OBJECTIVE:
Create a blockchain-based prescription tracking system that uses an LLM to validate
and analyze prescription data before adding it to the blockchain.

LEARNING OUTCOMES:
1. Understand blockchain basics (blocks, hashing, chain validation)
2. Integrate AI/LLM for data validation
3. Implement healthcare data security concepts
4. Combine distributed ledger technology with intelligent analysis

SYSTEM ARCHITECTURE:
- Blockchain: Stores validated prescription records
- LLM Agent: Validates prescription data for safety and completeness
- API Interface: Handles prescription submissions

Author: Your Name
Date: November 2025
Version: 1.0
"""

import hashlib
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from collections import defaultdict
import math
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from queue import PriorityQueue
import time
import random
import io


# ============================================================================
# PART 1: BLOCKCHAIN IMPLEMENTATION
# ============================================================================

class Block:
    """
    Represents a single block in the blockchain.
    
    Each block contains:
    - index: Position in the chain
    - timestamp: When the block was created
    - prescription_data: The prescription information
    - validation_report: AI validation results
    - previous_hash: Hash of the previous block (creates the chain)
    - hash: This block's unique identifier
    """
    
    def __init__(self, index: int, timestamp: str, prescription_data: Dict, 
                 previous_hash: str, validation_report: Dict):
        """
        Initialize a new block.
        
        Args:
            index: Block number in the chain
            timestamp: ISO format timestamp
            prescription_data: Dictionary containing prescription details
            previous_hash: Hash of the previous block
            validation_report: AI validation results
        """
        self.index = index
        self.timestamp = timestamp
        self.prescription_data = prescription_data
        self.validation_report = validation_report
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """
        Calculate SHA-256 hash of block contents.
        
        This hash uniquely identifies the block and ensures data integrity.
        Any change to the block's data will result in a completely different hash.
        
        Returns:
            str: 64-character hexadecimal hash string
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "prescription_data": self.prescription_data,
            "validation_report": self.validation_report,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def to_dict(self) -> Dict:
        """
        Convert block to dictionary for easy serialization and display.
        
        Returns:
            dict: Block data as a dictionary
        """
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "prescription_data": self.prescription_data,
            "validation_report": self.validation_report,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }


class PrescriptionBlockchain:
    """
    Manages the prescription blockchain.
    
    This class handles:
    - Creating and maintaining the chain
    - Adding new blocks
    - Validating chain integrity
    - Querying prescription history
    """
    
    def __init__(self):
        """Initialize the blockchain with a genesis block."""
        self.chain: List[Block] = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """
        Create the first block in the chain (genesis block).
        
        The genesis block is the foundation of the blockchain and has
        a previous_hash of "0" since there's no block before it.
        """
        genesis_block = Block(
            index=0,
            timestamp=datetime.now().isoformat(),
            prescription_data={"type": "genesis"},
            previous_hash="0",
            validation_report={"status": "genesis_block"}
        )
        self.chain.append(genesis_block)
        print(f"✓ Genesis block created with hash: {genesis_block.hash[:16]}...")
    
    def get_latest_block(self) -> Block:
        """
        Return the most recent block in the chain.
        
        Returns:
            Block: The last block in the chain
        """
        return self.chain[-1]
    
    def add_block(self, prescription_data: Dict, validation_report: Dict) -> Block:
        """
        Add a new validated prescription block to the chain.
        
        Args:
            prescription_data: Dictionary containing prescription information
            validation_report: AI validation results
            
        Returns:
            Block: The newly created block
        """
        new_block = Block(
            index=len(self.chain),
            timestamp=datetime.now().isoformat(),
            prescription_data=prescription_data,
            previous_hash=self.get_latest_block().hash,
            validation_report=validation_report
        )
        self.chain.append(new_block)
        return new_block
    
    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the entire blockchain.
        
        This checks:
        1. Each block's hash is correct (no data tampering)
        2. Each block's previous_hash matches the actual previous block
        
        Returns:
            bool: True if chain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Check if the block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                print(f"✗ Invalid hash at block {i}")
                return False
            
            # Check if previous_hash matches
            if current_block.previous_hash != previous_block.hash:
                print(f"✗ Invalid previous_hash link at block {i}")
                return False
        
        return True
    
    def get_patient_history(self, patient_id: str) -> List[Dict]:
        """
        Retrieve all prescriptions for a specific patient.
        
        Args:
            patient_id: The patient's unique identifier
            
        Returns:
            list: List of prescription records for the patient
        """
        return [
            block.to_dict() 
            for block in self.chain[1:]  # Skip genesis block
            if block.prescription_data.get("patient_id") == patient_id
        ]
    
    def get_doctor_prescriptions(self, doctor_id: str) -> List[Dict]:
        """
        Retrieve all prescriptions written by a specific doctor.
        
        Args:
            doctor_id: The doctor's unique identifier
            
        Returns:
            list: List of prescription records by the doctor
        """
        return [
            block.to_dict() 
            for block in self.chain[1:]
            if block.prescription_data.get("doctor_id") == doctor_id
        ]
    
    def search_by_medication(self, medication_name: str) -> List[Dict]:
        """
        Search for prescriptions by medication name.
        
        Args:
            medication_name: Name of the medication to search for
            
        Returns:
            list: List of prescription records containing the medication
        """
        medication_lower = medication_name.lower()
        return [
            block.to_dict() 
            for block in self.chain[1:]
            if medication_lower in block.prescription_data.get("medication", "").lower()
        ]


# ============================================================================
# PART 2: ALERT & NOTIFICATION SYSTEM
# ============================================================================

class AlertNotificationSystem:
    """
    Handles email, SMS, and system alerts for flagged prescriptions.
    
    Supports multiple notification channels:
    - Email alerts to pharmacists, doctors, compliance officers
    - SMS alerts for urgent/critical cases
    - System notifications logged for audit trail
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize the alert system.
        
        Args:
            config: Configuration dictionary with email/SMS settings
        """
        self.config = config or self._default_config()
        self.alert_log = []
    
    def _default_config(self) -> Dict:
        """Return default configuration."""
        return {
            "email": {
                "enabled": True,
                "smtp_server": "smtp.gmail.com",
                "smtp_port": 587,
                "sender_email": "pharmacy-alerts@hospital.com",
                "sender_password": "your-password-here",
                # In production, use environment variables for credentials
            },
            "sms": {
                "enabled": True,
                "api_endpoint": "https://api.sms-service.com/send",
                "api_key": "your-sms-api-key",
            },
            "recipients": {
                "critical": {
                    "email": ["compliance@hospital.com", "chief-pharmacist@hospital.com"],
                    "sms": ["+1-555-0100", "+1-555-0101"]
                },
                "high": {
                    "email": ["pharmacy-manager@hospital.com"],
                    "sms": ["+1-555-0100"]
                },
                "moderate": {
                    "email": ["pharmacist-on-duty@hospital.com"],
                    "sms": []
                }
            }
        }
    
    def send_alert(self, alert_level: str, prescription_data: Dict, 
                   risk_assessment: Dict, submission_result: Dict) -> Dict:
        """
        Send alerts via configured channels.
        
        Args:
            alert_level: "CRITICAL", "HIGH", or "MODERATE"
            prescription_data: The prescription information
            risk_assessment: Misuse risk analysis results
            submission_result: Result from prescription submission
            
        Returns:
            dict: Alert delivery status
        """
        alert_id = f"ALERT-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        
        alert_record = {
            "alert_id": alert_id,
            "timestamp": datetime.now().isoformat(),
            "alert_level": alert_level,
            "prescription_data": prescription_data,
            "risk_assessment": risk_assessment,
            "submission_result": submission_result,
            "notifications_sent": []
        }
        
        # Send email alerts
        if self.config["email"]["enabled"]:
            email_result = self._send_email_alert(alert_level, prescription_data, 
                                                   risk_assessment, alert_id)
            alert_record["notifications_sent"].append(email_result)
        
        # Send SMS alerts
        if self.config["sms"]["enabled"]:
            sms_result = self._send_sms_alert(alert_level, prescription_data, 
                                              risk_assessment, alert_id)
            alert_record["notifications_sent"].append(sms_result)
        
        # Log system notification
        system_notification = self._create_system_notification(
            alert_level, prescription_data, risk_assessment, alert_id
        )
        alert_record["notifications_sent"].append(system_notification)
        
        # Store in alert log
        self.alert_log.append(alert_record)
        
        return alert_record
    
    def _send_email_alert(self, alert_level: str, prescription_data: Dict,
                          risk_assessment: Dict, alert_id: str) -> Dict:
        """Send email alert (simulated in this demo)."""
        recipients = self.config["recipients"].get(
            alert_level.lower().replace(" ", "_"), 
            self.config["recipients"]["moderate"]
        )["email"]
        
        subject = f"🚨 {alert_level} ALERT: Prescription Flagged [{alert_id}]"
        
        body = f"""
PRESCRIPTION ALERT NOTIFICATION
{'='*70}

Alert ID: {alert_id}
Alert Level: {alert_level}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

PATIENT INFORMATION:
  Name: {prescription_data.get('patient_name', 'N/A')}
  ID: {prescription_data.get('patient_id', 'N/A')}
  Age: {prescription_data.get('patient_age', 'N/A')}

PRESCRIPTION DETAILS:
  Medication: {prescription_data.get('medication', 'N/A')}
  Dosage: {prescription_data.get('dosage', 'N/A')}
  Duration: {prescription_data.get('duration', 'N/A')}
  Doctor: {prescription_data.get('doctor_name', 'N/A')} (ID: {prescription_data.get('doctor_id', 'N/A')})

RISK ASSESSMENT:
  Risk Level: {risk_assessment.get('risk_level', 'N/A')}
  Risk Score: {risk_assessment.get('risk_score', 0)}/100
  
  Risk Factors:
{chr(10).join('    - ' + factor for factor in risk_assessment.get('risk_factors', ['None']))}

RECOMMENDATIONS:
{chr(10).join('  • ' + rec for rec in risk_assessment.get('recommendations', ['None'])[:5])}

ACTION REQUIRED:
  {'⛔ IMMEDIATE REVIEW REQUIRED - Prescription has been BLOCKED' if alert_level == 'CRITICAL' else '⚠️  Manual review recommended before dispensing'}

{'='*70}
This is an automated alert from the Prescription Tracking System.
For questions, contact the pharmacy compliance department.
        """
        
        # In production, actually send the email:
        # try:
        #     msg = MIMEMultipart()
        #     msg['From'] = self.config["email"]["sender_email"]
        #     msg['To'] = ", ".join(recipients)
        #     msg['Subject'] = subject
        #     msg.attach(MIMEText(body, 'plain'))
        #     
        #     server = smtplib.SMTP(self.config["email"]["smtp_server"], 
        #                          self.config["email"]["smtp_port"])
        #     server.starttls()
        #     server.login(self.config["email"]["sender_email"],
        #                  self.config["email"]["sender_password"])
        #     server.send_message(msg)
        #     server.quit()
        #     status = "sent"
        # except Exception as e:
        #     status = f"failed: {str(e)}"
        
        # For demo purposes, just simulate
        print(f"\n  📧 EMAIL ALERT SENT:")
        print(f"     To: {', '.join(recipients)}")
        print(f"     Subject: {subject}")
        
        return {
            "type": "email",
            "status": "simulated_sent",
            "recipients": recipients,
            "timestamp": datetime.now().isoformat()
        }
    
    def _send_sms_alert(self, alert_level: str, prescription_data: Dict,
                       risk_assessment: Dict, alert_id: str) -> Dict:
        """Send SMS alert (simulated in this demo)."""
        recipients = self.config["recipients"].get(
            alert_level.lower().replace(" ", "_"),
            {"sms": []}
        )["sms"]
        
        if not recipients:
            return {
                "type": "sms",
                "status": "skipped",
                "reason": "no recipients configured"
            }
        
        message = (
            f"🚨 {alert_level} ALERT [{alert_id}]\n"
            f"Patient: {prescription_data.get('patient_name', 'N/A')}\n"
            f"Medication: {prescription_data.get('medication', 'N/A')}\n"
            f"Risk Score: {risk_assessment.get('risk_score', 0)}/100\n"
            f"Action: {'BLOCKED - Review required' if alert_level == 'CRITICAL' else 'Review recommended'}"
        )
        
        # In production, send via SMS API:
        # try:
        #     response = requests.post(
        #         self.config["sms"]["api_endpoint"],
        #         headers={"Authorization": f"Bearer {self.config['sms']['api_key']}"},
        #         json={"to": recipients, "message": message}
        #     )
        #     status = "sent" if response.status_code == 200 else "failed"
        # except Exception as e:
        #     status = f"failed: {str(e)}"
        
        # For demo purposes, just simulate
        print(f"\n  📱 SMS ALERT SENT:")
        print(f"     To: {', '.join(recipients)}")
        print(f"     Message: {message[:100]}...")
        
        return {
            "type": "sms",
            "status": "simulated_sent",
            "recipients": recipients,
            "timestamp": datetime.now().isoformat()
        }
    
    def _create_system_notification(self, alert_level: str, prescription_data: Dict,
                                    risk_assessment: Dict, alert_id: str) -> Dict:
        """Create system notification for audit log."""
        return {
            "type": "system",
            "status": "logged",
            "alert_id": alert_id,
            "timestamp": datetime.now().isoformat(),
            "message": f"{alert_level} alert generated for patient {prescription_data.get('patient_id')}"
        }
    
    def get_alert_history(self, limit: int = 50) -> List[Dict]:
        """Retrieve recent alert history."""
        return self.alert_log[-limit:]
    
    def get_alerts_by_level(self, alert_level: str) -> List[Dict]:
        """Retrieve alerts by severity level."""
        return [
            alert for alert in self.alert_log 
            if alert["alert_level"] == alert_level
        ]


# ============================================================================
# PART 3: REVIEW QUEUE SYSTEM
# ============================================================================

class ReviewQueue:
    """
    Manages flagged prescriptions requiring manual review.
    
    Features:
    - Priority-based queue (CRITICAL > HIGH > MODERATE)
    - Status tracking (pending, under_review, approved, rejected)
    - Assignment to reviewers
    - SLA tracking (time in queue)
    """
    
    def __init__(self):
        """Initialize the review queue."""
        self.queue = []
        self.reviewed_items = []
        self.queue_id_counter = 1
    
    def add_to_queue(self, prescription_data: Dict, risk_assessment: Dict,
                     validation_report: Dict, alert_level: str) -> Dict:
        """
        Add a flagged prescription to the review queue.
        
        Args:
            prescription_data: The prescription information
            risk_assessment: Misuse risk analysis
            validation_report: Validation results
            alert_level: Severity level
            
        Returns:
            dict: Queue item with tracking information
        """
        # Priority: CRITICAL=1, HIGH=2, MODERATE=3 (lower number = higher priority)
        priority_map = {"CRITICAL": 1, "HIGH": 2, "MODERATE": 3}
        priority = priority_map.get(alert_level, 3)
        
        queue_item = {
            "queue_id": f"RQ-{self.queue_id_counter:05d}",
            "added_timestamp": datetime.now().isoformat(),
            "priority": priority,
            "alert_level": alert_level,
            "status": "pending",
            "prescription_data": prescription_data,
            "risk_assessment": risk_assessment,
            "validation_report": validation_report,
            "assigned_to": None,
            "review_notes": [],
            "sla_deadline": (datetime.now() + timedelta(hours=2 if priority == 1 else 24)).isoformat()
        }
        
        self.queue.append(queue_item)
        self.queue_id_counter += 1
        
        # Sort queue by priority
        self.queue.sort(key=lambda x: (x["priority"], x["added_timestamp"]))
        
        return queue_item
    
    def get_next_item(self) -> Optional[Dict]:
        """Get the highest priority pending item."""
        for item in self.queue:
            if item["status"] == "pending":
                return item
        return None
    
    def assign_to_reviewer(self, queue_id: str, reviewer_name: str) -> bool:
        """Assign a queue item to a reviewer."""
        for item in self.queue:
            if item["queue_id"] == queue_id and item["status"] == "pending":
                item["status"] = "under_review"
                item["assigned_to"] = reviewer_name
                item["review_started"] = datetime.now().isoformat()
                return True
        return False
    
    def complete_review(self, queue_id: str, decision: str, 
                       notes: str, reviewer_name: str) -> Dict:
        """
        Complete review of a flagged prescription.
        
        Args:
            queue_id: Queue item identifier
            decision: "approved" or "rejected"
            notes: Reviewer's notes
            reviewer_name: Name of the reviewer
            
        Returns:
            dict: Review result
        """
        for i, item in enumerate(self.queue):
            if item["queue_id"] == queue_id:
                item["status"] = decision
                item["review_completed"] = datetime.now().isoformat()
                item["final_decision"] = decision
                item["review_notes"].append({
                    "timestamp": datetime.now().isoformat(),
                    "reviewer": reviewer_name,
                    "notes": notes
                })
                
                # Calculate review time
                start_time = datetime.fromisoformat(item.get("review_started", item["added_timestamp"]))
                end_time = datetime.now()
                item["review_duration_minutes"] = int((end_time - start_time).total_seconds() / 60)
                
                # Move to reviewed items
                reviewed_item = self.queue.pop(i)
                self.reviewed_items.append(reviewed_item)
                
                return reviewed_item
        
        return {"error": "Queue item not found"}
    
    def get_queue_status(self) -> Dict:
        """Get overall queue statistics."""
        pending = sum(1 for item in self.queue if item["status"] == "pending")
        under_review = sum(1 for item in self.queue if item["status"] == "under_review")
        
        # Check SLA violations
        sla_violations = 0
        for item in self.queue:
            if item["status"] in ["pending", "under_review"]:
                deadline = datetime.fromisoformat(item["sla_deadline"])
                if datetime.now() > deadline:
                    sla_violations += 1
        
        return {
            "pending": pending,
            "under_review": under_review,
            "total_in_queue": len(self.queue),
            "total_reviewed": len(self.reviewed_items),
            "sla_violations": sla_violations
        }
    
    def get_queue_items(self, status: Optional[str] = None) -> List[Dict]:
        """Get queue items, optionally filtered by status."""
        if status:
            return [item for item in self.queue if item["status"] == status]
        return self.queue.copy()
    
    def get_overdue_items(self) -> List[Dict]:
        """Get items that have exceeded their SLA deadline."""
        now = datetime.now()
        return [
            item for item in self.queue
            if item["status"] in ["pending", "under_review"] and
            datetime.fromisoformat(item["sla_deadline"]) < now
        ]


# ============================================================================
# PART 4: ESCALATION WORKFLOW SYSTEM
# ============================================================================

class EscalationWorkflow:
    """
    Manages escalation of prescription reviews based on severity and time.
    
    Escalation Rules:
    - CRITICAL: Immediate notification to compliance officer + chief pharmacist
    - HIGH: Notification to pharmacy manager after 1 hour if unreviewed
    - MODERATE: Notification to senior pharmacist after 4 hours
    - Any item: Escalate one level up if unreviewed past SLA
    """
    
    def __init__(self, alert_system: AlertNotificationSystem, 
                 review_queue: ReviewQueue):
        """Initialize escalation workflow."""
        self.alert_system = alert_system
        self.review_queue = review_queue
        self.escalation_log = []
    
    def check_escalations(self) -> List[Dict]:
        """
        Check for items requiring escalation.
        
        Returns:
            list: Items that were escalated
        """
        escalated_items = []
        now = datetime.now()
        
        for item in self.review_queue.queue:
            if item["status"] not in ["pending", "under_review"]:
                continue
            
            added_time = datetime.fromisoformat(item["added_timestamp"])
            time_in_queue = (now - added_time).total_seconds() / 3600  # hours
            
            escalation_needed = False
            escalation_reason = ""
            new_level = item["alert_level"]
            
            # Rule 1: CRITICAL items not assigned within 15 minutes
            if item["alert_level"] == "CRITICAL" and item["status"] == "pending" and time_in_queue > 0.25:
                escalation_needed = True
                escalation_reason = "CRITICAL item unassigned for >15 minutes"
            
            # Rule 2: HIGH items not reviewed within 1 hour
            elif item["alert_level"] == "HIGH" and time_in_queue > 1:
                escalation_needed = True
                escalation_reason = "HIGH priority item unreviewed for >1 hour"
                new_level = "CRITICAL"
            
            # Rule 3: MODERATE items not reviewed within 4 hours
            elif item["alert_level"] == "MODERATE" and time_in_queue > 4:
                escalation_needed = True
                escalation_reason = "MODERATE priority item unreviewed for >4 hours"
                new_level = "HIGH"
            
            # Rule 4: Any item past SLA deadline
            sla_deadline = datetime.fromisoformat(item["sla_deadline"])
            if now > sla_deadline and item["status"] == "pending":
                escalation_needed = True
                escalation_reason = "SLA deadline exceeded"
                # Escalate one level
                if item["alert_level"] == "MODERATE":
                    new_level = "HIGH"
                elif item["alert_level"] == "HIGH":
                    new_level = "CRITICAL"
            
            if escalation_needed:
                escalation_record = self._escalate_item(
                    item, escalation_reason, new_level
                )
                escalated_items.append(escalation_record)
        
        return escalated_items
    
    def _escalate_item(self, item: Dict, reason: str, new_level: str) -> Dict:
        """Escalate a queue item to higher priority."""
        escalation_record = {
            "escalation_id": f"ESC-{len(self.escalation_log) + 1:05d}",
            "timestamp": datetime.now().isoformat(),
            "queue_id": item["queue_id"],
            "original_level": item["alert_level"],
            "escalated_to": new_level,
            "reason": reason,
            "patient_id": item["prescription_data"].get("patient_id"),
            "medication": item["prescription_data"].get("medication")
        }
        
        # Update item in queue
        item["alert_level"] = new_level
        item["escalation_history"] = item.get("escalation_history", [])
        item["escalation_history"].append(escalation_record)
        
        # Send escalation notification
        print(f"\n  ⚠️  ESCALATION TRIGGERED:")
        print(f"     Queue ID: {item['queue_id']}")
        print(f"     Reason: {reason}")
        print(f"     Escalated: {escalation_record['original_level']} → {new_level}")
        
        # Send alerts to higher-level recipients
        self.alert_system.send_alert(
            new_level,
            item["prescription_data"],
            item["risk_assessment"],
            {"status": "escalated", "reason": reason}
        )
        
        self.escalation_log.append(escalation_record)
        return escalation_record
    
    def get_escalation_history(self) -> List[Dict]:
        """Get all escalation records."""
        return self.escalation_log.copy()


# ============================================================================
# PART 5: PRESCRIPTION MISUSE PREDICTION MODEL
# ============================================================================

class MisusePredictionModel:
    """
    Machine Learning model to predict potential prescription misuse.
    
    This model analyzes patterns in prescription data to identify:
    - Doctor shopping (multiple doctors for same medication)
    - Excessive dosages
    - Early refills
    - High-risk medication combinations
    - Unusual prescription frequency
    
    Risk Scoring:
    - 0-30: Low risk
    - 31-60: Moderate risk
    - 61-100: High risk (potential misuse)
    """
    
    # High-risk medications (controlled substances, opioids, etc.)
    HIGH_RISK_MEDICATIONS = [
        "Oxycodone", "Hydrocodone", "Fentanyl", "Morphine", "Codeine",
        "Xanax", "Alprazolam", "Diazepam", "Lorazepam", "Clonazepam",
        "Adderall", "Ritalin", "Vyvanse", "Ambien", "Tramadol"
    ]
    
    # Training data: Historical patterns of misuse
    TRAINING_DATA = {
        "normal_patterns": {
            "avg_prescriptions_per_month": 2.0,
            "avg_doctors_per_medication": 1.0,
            "avg_dosage_multiplier": 1.0,
            "avg_days_between_refills": 30.0
        },
        "misuse_patterns": {
            "avg_prescriptions_per_month": 6.5,
            "avg_doctors_per_medication": 3.2,
            "avg_dosage_multiplier": 2.1,
            "avg_days_between_refills": 12.0
        }
    }
    
    def __init__(self):
        """Initialize the misuse prediction model."""
        self.weights = {
            "prescription_frequency": 0.25,
            "doctor_shopping": 0.30,
            "high_dosage": 0.20,
            "early_refill": 0.15,
            "high_risk_medication": 0.10
        }
    
    def predict_misuse_risk(self, patient_history: List[Dict], 
                           current_prescription: Dict) -> Dict:
        """
        Predict the risk of prescription misuse.
        
        Args:
            patient_history: List of previous prescriptions for the patient
            current_prescription: The new prescription being evaluated
            
        Returns:
            dict: Risk assessment with score and details
        """
        risk_score = 0
        risk_factors = []
        recommendations = []
        
        # Feature 1: Prescription Frequency
        freq_score, freq_factors = self._analyze_prescription_frequency(
            patient_history, current_prescription
        )
        risk_score += freq_score * self.weights["prescription_frequency"]
        risk_factors.extend(freq_factors)
        
        # Feature 2: Doctor Shopping
        doctor_score, doctor_factors = self._analyze_doctor_shopping(
            patient_history, current_prescription
        )
        risk_score += doctor_score * self.weights["doctor_shopping"]
        risk_factors.extend(doctor_factors)
        
        # Feature 3: High Dosage Analysis
        dosage_score, dosage_factors = self._analyze_dosage_pattern(
            patient_history, current_prescription
        )
        risk_score += dosage_score * self.weights["high_dosage"]
        risk_factors.extend(dosage_factors)
        
        # Feature 4: Early Refill Detection
        refill_score, refill_factors = self._analyze_refill_pattern(
            patient_history, current_prescription
        )
        risk_score += refill_score * self.weights["early_refill"]
        risk_factors.extend(refill_factors)
        
        # Feature 5: High-Risk Medication
        medication_score, med_factors = self._analyze_medication_risk(
            current_prescription
        )
        risk_score += medication_score * self.weights["high_risk_medication"]
        risk_factors.extend(med_factors)
        
        # Determine risk level
        risk_level = self._determine_risk_level(risk_score)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            risk_level, risk_factors
        )
        
        return {
            "risk_score": round(risk_score, 2),
            "risk_level": risk_level,
            "risk_factors": risk_factors,
            "recommendations": recommendations,
            "analysis_timestamp": datetime.now().isoformat(),
            "model_version": "1.0"
        }
    
    def _analyze_prescription_frequency(self, history: List[Dict], 
                                       current: Dict) -> Tuple[float, List[str]]:
        """Analyze how frequently the patient receives prescriptions."""
        if not history:
            return 0.0, []
        
        # Count prescriptions in last 30 days
        recent_prescriptions = 0
        cutoff_date = datetime.now() - timedelta(days=30)
        
        for record in history:
            timestamp = datetime.fromisoformat(record['timestamp'])
            if timestamp >= cutoff_date:
                recent_prescriptions += 1
        
        score = 0
        factors = []
        
        if recent_prescriptions >= 6:
            score = 100
            factors.append(f"🚨 CRITICAL: {recent_prescriptions} prescriptions in 30 days (normal: 1-2)")
        elif recent_prescriptions >= 4:
            score = 70
            factors.append(f"⚠️ HIGH: {recent_prescriptions} prescriptions in 30 days")
        elif recent_prescriptions >= 3:
            score = 40
            factors.append(f"⚠️ MODERATE: {recent_prescriptions} prescriptions in 30 days")
        
        return score, factors
    
    def _analyze_doctor_shopping(self, history: List[Dict], 
                                 current: Dict) -> Tuple[float, List[str]]:
        """Detect if patient is visiting multiple doctors for same medication."""
        medication = current.get("medication", "").lower()
        current_doctor = current.get("doctor_id")
        
        # Track doctors who prescribed the same medication
        doctors_for_medication = set()
        
        for record in history:
            record_med = record['prescription_data'].get('medication', '').lower()
            record_doctor = record['prescription_data'].get('doctor_id')
            
            if medication in record_med or record_med in medication:
                doctors_for_medication.add(record_doctor)
        
        # Add current doctor
        doctors_for_medication.add(current_doctor)
        
        score = 0
        factors = []
        
        num_doctors = len(doctors_for_medication)
        if num_doctors >= 4:
            score = 100
            factors.append(f"🚨 CRITICAL: {num_doctors} different doctors for same medication (doctor shopping)")
        elif num_doctors >= 3:
            score = 75
            factors.append(f"⚠️ HIGH: {num_doctors} different doctors for same medication")
        elif num_doctors >= 2:
            score = 40
            factors.append(f"⚠️ MODERATE: {num_doctors} doctors for same medication")
        
        return score, factors
    
    def _analyze_dosage_pattern(self, history: List[Dict], 
                               current: Dict) -> Tuple[float, List[str]]:
        """Analyze if dosage is unusually high or escalating."""
        dosage_str = current.get("dosage", "")
        
        # Extract numeric dosage
        current_dosage = self._extract_dosage_number(dosage_str)
        
        if current_dosage is None:
            return 0.0, []
        
        # Check historical dosages for same medication
        medication = current.get("medication", "").lower()
        historical_dosages = []
        
        for record in history:
            record_med = record['prescription_data'].get('medication', '').lower()
            if medication in record_med or record_med in medication:
                hist_dosage = self._extract_dosage_number(
                    record['prescription_data'].get('dosage', '')
                )
                if hist_dosage:
                    historical_dosages.append(hist_dosage)
        
        score = 0
        factors = []
        
        if historical_dosages:
            avg_dosage = sum(historical_dosages) / len(historical_dosages)
            dosage_ratio = current_dosage / avg_dosage if avg_dosage > 0 else 1.0
            
            if dosage_ratio >= 2.5:
                score = 100
                factors.append(f"🚨 CRITICAL: Dosage {dosage_ratio:.1f}x higher than patient's average")
            elif dosage_ratio >= 2.0:
                score = 70
                factors.append(f"⚠️ HIGH: Dosage {dosage_ratio:.1f}x higher than usual")
            elif dosage_ratio >= 1.5:
                score = 40
                factors.append(f"⚠️ MODERATE: Dosage increase of {dosage_ratio:.1f}x detected")
        
        return score, factors
    
    def _analyze_refill_pattern(self, history: List[Dict], 
                               current: Dict) -> Tuple[float, List[str]]:
        """Detect early refill patterns that suggest misuse."""
        medication = current.get("medication", "").lower()
        
        # Find most recent prescription for same medication
        for record in reversed(history):
            record_med = record['prescription_data'].get('medication', '').lower()
            if medication in record_med or record_med in medication:
                last_prescription_date = datetime.fromisoformat(record['timestamp'])
                days_since_last = (datetime.now() - last_prescription_date).days
                
                duration_str = record['prescription_data'].get('duration', '30 days')
                expected_days = self._extract_duration_days(duration_str)
                
                score = 0
                factors = []
                
                if days_since_last < expected_days * 0.5:
                    score = 100
                    factors.append(f"🚨 CRITICAL: Refill after {days_since_last} days (expected: {expected_days})")
                elif days_since_last < expected_days * 0.7:
                    score = 70
                    factors.append(f"⚠️ HIGH: Early refill at {days_since_last} days")
                elif days_since_last < expected_days * 0.9:
                    score = 40
                    factors.append(f"⚠️ MODERATE: Slightly early refill")
                
                return score, factors
        
        return 0.0, []
    
    def _analyze_medication_risk(self, current: Dict) -> Tuple[float, List[str]]:
        """Check if medication is high-risk (controlled substance)."""
        medication = current.get("medication", "")
        
        for high_risk_med in self.HIGH_RISK_MEDICATIONS:
            if high_risk_med.lower() in medication.lower():
                return 100, [f"⚠️ Controlled substance: {high_risk_med}"]
        
        return 0.0, []
    
    def _extract_dosage_number(self, dosage_str: str) -> Optional[float]:
        """Extract numeric dosage from dosage string."""
        import re
        match = re.search(r'(\d+(?:\.\d+)?)', dosage_str)
        if match:
            return float(match.group(1))
        return None
    
    def _extract_duration_days(self, duration_str: str) -> int:
        """Extract number of days from duration string."""
        import re
        match = re.search(r'(\d+)', duration_str)
        if match:
            return int(match.group(1))
        return 30  # Default
    
    def _determine_risk_level(self, score: float) -> str:
        """Determine risk level based on score."""
        if score >= 61:
            return "HIGH RISK"
        elif score >= 31:
            return "MODERATE RISK"
        else:
            return "LOW RISK"
    
    def _generate_recommendations(self, risk_level: str, 
                                 risk_factors: List[str]) -> List[str]:
        """Generate recommendations based on risk assessment."""
        recommendations = []
        
        if risk_level == "HIGH RISK":
            recommendations.append("🔴 IMMEDIATE ACTION REQUIRED")
            recommendations.append("Contact prescribing physician for verification")
            recommendations.append("Review patient's complete prescription history")
            recommendations.append("Consider requiring in-person consultation")
            recommendations.append("Alert pharmacy manager for review")
        elif risk_level == "MODERATE RISK":
            recommendations.append("🟡 Enhanced monitoring recommended")
            recommendations.append("Verify prescription with doctor's office")
            recommendations.append("Counsel patient on proper medication use")
            recommendations.append("Document any concerns in patient file")
        else:
            recommendations.append("🟢 Standard dispensing procedures apply")
            recommendations.append("Provide routine patient counseling")
        
        return recommendations


# ============================================================================
# PART 6: PERFORMANCE METRICS & REPORTING
# ============================================================================

class PerformanceMetrics:
    """
    Tracks and reports system performance metrics.
    
    Metrics tracked:
    - Processing times (validation, blockchain writes)
    - Throughput (prescriptions per hour)
    - Alert response times
    - Queue efficiency
    - System availability
    - Error rates
    """
    
    def __init__(self):
        """Initialize performance metrics tracker."""
        self.metrics = {
            "total_prescriptions_processed": 0,
            "total_validations": 0,
            "total_blockchain_writes": 0,
            "total_alerts_sent": 0,
            "total_reviews_completed": 0,
            "processing_times": [],
            "validation_times": [],
            "blockchain_write_times": [],
            "alert_response_times": [],
            "queue_wait_times": [],
            "errors": [],
            "start_time": datetime.now(),
            "hourly_throughput": defaultdict(int)
        }
    
    def record_prescription_processing(self, processing_time: float, success: bool):
        """Record prescription processing metrics."""
        self.metrics["total_prescriptions_processed"] += 1
        self.metrics["processing_times"].append(processing_time)
        
        # Track hourly throughput
        hour_key = datetime.now().strftime("%Y-%m-%d %H:00")
        self.metrics["hourly_throughput"][hour_key] += 1
        
        if not success:
            self.metrics["errors"].append({
                "timestamp": datetime.now().isoformat(),
                "type": "processing_error",
                "processing_time": processing_time
            })
    
    def record_validation(self, validation_time: float):
        """Record validation metrics."""
        self.metrics["total_validations"] += 1
        self.metrics["validation_times"].append(validation_time)
    
    def record_blockchain_write(self, write_time: float):
        """Record blockchain write metrics."""
        self.metrics["total_blockchain_writes"] += 1
        self.metrics["blockchain_write_times"].append(write_time)
    
    def record_alert(self, response_time: float):
        """Record alert metrics."""
        self.metrics["total_alerts_sent"] += 1
        self.metrics["alert_response_times"].append(response_time)
    
    def record_review(self, wait_time: float):
        """Record review metrics."""
        self.metrics["total_reviews_completed"] += 1
        self.metrics["queue_wait_times"].append(wait_time)
    
    def get_summary_report(self) -> Dict:
        """Generate comprehensive performance report."""
        uptime = (datetime.now() - self.metrics["start_time"]).total_seconds()
        uptime_hours = uptime / 3600
        
        def safe_avg(lst):
            return sum(lst) / len(lst) if lst else 0
        
        def safe_percentile(lst, percentile):
            if not lst:
                return 0
            sorted_lst = sorted(lst)
            index = int(len(sorted_lst) * percentile / 100)
            return sorted_lst[min(index, len(sorted_lst) - 1)]
        
        return {
            "system_uptime_hours": round(uptime_hours, 2),
            "total_prescriptions": self.metrics["total_prescriptions_processed"],
            "throughput_per_hour": round(self.metrics["total_prescriptions_processed"] / uptime_hours, 2) if uptime_hours > 0 else 0,
            "processing_times": {
                "average_ms": round(safe_avg(self.metrics["processing_times"]) * 1000, 2),
                "p50_ms": round(safe_percentile(self.metrics["processing_times"], 50) * 1000, 2),
                "p95_ms": round(safe_percentile(self.metrics["processing_times"], 95) * 1000, 2),
                "p99_ms": round(safe_percentile(self.metrics["processing_times"], 99) * 1000, 2)
            },
            "validation_times": {
                "average_ms": round(safe_avg(self.metrics["validation_times"]) * 1000, 2),
                "total_validations": self.metrics["total_validations"]
            },
            "blockchain_performance": {
                "average_write_ms": round(safe_avg(self.metrics["blockchain_write_times"]) * 1000, 2),
                "total_writes": self.metrics["total_blockchain_writes"]
            },
            "alert_performance": {
                "average_response_ms": round(safe_avg(self.metrics["alert_response_times"]) * 1000, 2),
                "total_alerts": self.metrics["total_alerts_sent"]
            },
            "queue_performance": {
                "average_wait_minutes": round(safe_avg(self.metrics["queue_wait_times"]), 2),
                "total_reviews": self.metrics["total_reviews_completed"]
            },
            "error_rate": round(len(self.metrics["errors"]) / max(self.metrics["total_prescriptions_processed"], 1) * 100, 2),
            "availability_percent": 99.9  # Simulated - would track actual downtime
        }
    
    def get_hourly_throughput(self) -> Dict:
        """Get prescriptions processed per hour."""
        return dict(self.metrics["hourly_throughput"])
    
    def print_performance_report(self):
        """Print formatted performance report."""
        report = self.get_summary_report()
        
        print(f"\n{'='*70}")
        print("SYSTEM PERFORMANCE METRICS")
        print(f"{'='*70}")
        
        print(f"\n📊 OVERALL PERFORMANCE:")
        print(f"   System Uptime: {report['system_uptime_hours']} hours")
        print(f"   Total Prescriptions: {report['total_prescriptions']}")
        print(f"   Throughput: {report['throughput_per_hour']} prescriptions/hour")
        print(f"   Availability: {report['availability_percent']}%")
        print(f"   Error Rate: {report['error_rate']}%")
        
        print(f"\n⚡ PROCESSING PERFORMANCE:")
        print(f"   Average Time: {report['processing_times']['average_ms']} ms")
        print(f"   P50 (Median): {report['processing_times']['p50_ms']} ms")
        print(f"   P95: {report['processing_times']['p95_ms']} ms")
        print(f"   P99: {report['processing_times']['p99_ms']} ms")
        
        print(f"\n🔍 VALIDATION PERFORMANCE:")
        print(f"   Average Time: {report['validation_times']['average_ms']} ms")
        print(f"   Total Validations: {report['validation_times']['total_validations']}")
        
        print(f"\n⛓️  BLOCKCHAIN PERFORMANCE:")
        print(f"   Average Write Time: {report['blockchain_performance']['average_write_ms']} ms")
        print(f"   Total Writes: {report['blockchain_performance']['total_writes']}")
        
        print(f"\n🚨 ALERT PERFORMANCE:")
        print(f"   Average Response: {report['alert_performance']['average_response_ms']} ms")
        print(f"   Total Alerts: {report['alert_performance']['total_alerts']}")
        
        print(f"\n📋 QUEUE PERFORMANCE:")
        print(f"   Average Wait Time: {report['queue_performance']['average_wait_minutes']} minutes")
        print(f"   Total Reviews: {report['queue_performance']['total_reviews']}")
        
        print(f"\n{'='*70}\n")


# ============================================================================
# PART 7: EXTERNAL PHARMACY SYSTEM INTEGRATION
# ============================================================================

class PharmacySystemIntegration:
    """
    Integration layer for external pharmacy management systems.
    
    Supports integration with:
    - Electronic Health Records (EHR) systems
    - Pharmacy Management Systems (PMS)
    - Insurance verification systems
    - State Prescription Drug Monitoring Programs (PDMP)
    - Inventory management systems
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """Initialize pharmacy system integration."""
        self.config = config or self._default_config()
        self.integration_log = []
    
    def _default_config(self) -> Dict:
        """Return default integration configuration."""
        return {
            "ehr_system": {
                "enabled": True,
                "api_endpoint": "https://api.ehr-system.com/v1",
                "api_key": "your-ehr-api-key",
                "timeout": 5
            },
            "pms_system": {
                "enabled": True,
                "api_endpoint": "https://api.pharmacy-system.com/v1",
                "api_key": "your-pms-api-key",
                "timeout": 5
            },
            "pdmp": {
                "enabled": True,
                "api_endpoint": "https://api.state-pdmp.gov/v1",
                "api_key": "your-pdmp-api-key",
                "timeout": 10
            },
            "insurance": {
                "enabled": True,
                "api_endpoint": "https://api.insurance-verify.com/v1",
                "api_key": "your-insurance-api-key",
                "timeout": 5
            },
            "inventory": {
                "enabled": True,
                "api_endpoint": "https://api.inventory.com/v1",
                "api_key": "your-inventory-api-key",
                "timeout": 3
            }
        }
    
    def check_patient_history(self, patient_id: str) -> Dict:
        """
        Query EHR system for patient medical history.
        
        In production, this would make an actual API call:
        response = requests.get(
            f"{self.config['ehr_system']['api_endpoint']}/patients/{patient_id}/history",
            headers={"Authorization": f"Bearer {self.config['ehr_system']['api_key']}"},
            timeout=self.config['ehr_system']['timeout']
        )
        """
        print(f"   🔍 Checking EHR system for patient {patient_id}...")
        
        # Simulated response
        result = {
            "patient_id": patient_id,
            "allergies": ["Penicillin", "Sulfa drugs"],
            "chronic_conditions": ["Hypertension", "Type 2 Diabetes"],
            "recent_procedures": [],
            "active_medications": ["Lisinopril 10mg", "Metformin 500mg"],
            "last_updated": datetime.now().isoformat()
        }
        
        self._log_integration("EHR", "patient_history", patient_id, "success")
        return result
    
    def check_pdmp(self, patient_id: str, medication: str) -> Dict:
        """
        Check State PDMP for controlled substance history.
        
        Critical for detecting doctor shopping and prescription abuse.
        """
        print(f"   🔍 Checking PDMP for controlled substances...")
        
        # Simulated PDMP response
        result = {
            "patient_id": patient_id,
            "controlled_substance_history": [
                {
                    "medication": "Oxycodone",
                    "prescriber": "Dr. Michael Johnson",
                    "pharmacy": "Main Street Pharmacy",
                    "fill_date": "2025-11-01",
                    "quantity": 60
                }
            ],
            "total_prescribers_30_days": 2,
            "total_pharmacies_30_days": 1,
            "risk_flags": ["Multiple prescribers"],
            "last_updated": datetime.now().isoformat()
        }
        
        self._log_integration("PDMP", "controlled_substance_check", patient_id, "success")
        return result
    
    def verify_insurance(self, patient_id: str, prescription_data: Dict) -> Dict:
        """
        Verify insurance coverage for prescription.
        
        Returns:
        - Coverage status
        - Copay amount
        - Prior authorization requirements
        - Formulary alternatives
        """
        print(f"   💳 Verifying insurance coverage...")
        
        # Simulated insurance verification
        result = {
            "coverage_status": "covered",
            "copay_amount": 25.00,
            "prior_authorization_required": False,
            "formulary_tier": 2,
            "formulary_alternatives": ["Generic Lisinopril"],
            "estimated_cost": {
                "with_insurance": 25.00,
                "without_insurance": 89.99
            },
            "verification_timestamp": datetime.now().isoformat()
        }
        
        self._log_integration("Insurance", "coverage_verification", patient_id, "success")
        return result
    
    def check_inventory(self, medication: str, quantity: int) -> Dict:
        """
        Check pharmacy inventory for medication availability.
        
        Returns:
        - Current stock level
        - Expected restock date
        - Alternative locations
        """
        print(f"   📦 Checking inventory for {medication}...")
        
        # Simulated inventory check
        current_stock = random.randint(0, 200)
        result = {
            "medication": medication,
            "in_stock": current_stock >= quantity,
            "current_stock": current_stock,
            "requested_quantity": quantity,
            "expected_restock": (datetime.now() + timedelta(days=3)).isoformat() if current_stock < quantity else None,
            "alternative_locations": [
                {"location": "Downtown Pharmacy", "distance_miles": 2.3, "stock": 150},
                {"location": "West Side Pharmacy", "distance_miles": 4.1, "stock": 89}
            ] if current_stock < quantity else [],
            "check_timestamp": datetime.now().isoformat()
        }
        
        self._log_integration("Inventory", "stock_check", medication, "success")
        return result
    
    def send_to_pms(self, prescription_data: Dict, blockchain_hash: str) -> Dict:
        """
        Send approved prescription to Pharmacy Management System.
        
        This creates the actual prescription order in the pharmacy system.
        """
        print(f"   ➡️  Sending to Pharmacy Management System...")
        
        # Simulated PMS submission
        result = {
            "pms_order_id": f"PMS-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            "status": "pending_fulfillment",
            "blockchain_reference": blockchain_hash,
            "estimated_ready_time": (datetime.now() + timedelta(minutes=15)).isoformat(),
            "assigned_pharmacist": "PharmD Sarah Johnson",
            "submission_timestamp": datetime.now().isoformat()
        }
        
        self._log_integration("PMS", "prescription_submission", 
                            prescription_data.get('patient_id'), "success")
        return result
    
    def full_integration_workflow(self, prescription_data: Dict, 
                                  blockchain_hash: Optional[str] = None) -> Dict:
        """
        Execute complete external system integration workflow.
        
        Steps:
        1. Check EHR for patient history
        2. Verify PDMP for controlled substances
        3. Verify insurance coverage
        4. Check inventory availability
        5. Send to PMS if approved
        """
        print(f"\n{'='*70}")
        print("EXTERNAL SYSTEM INTEGRATION WORKFLOW")
        print(f"{'='*70}\n")
        
        patient_id = prescription_data.get('patient_id')
        medication = prescription_data.get('medication')
        
        results = {
            "workflow_id": f"WF-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            "timestamp": datetime.now().isoformat(),
            "prescription_data": prescription_data
        }
        
        # Step 1: EHR Check
        print("Step 1: Electronic Health Records Check")
        results["ehr_data"] = self.check_patient_history(patient_id)
        print(f"   ✓ Found {len(results['ehr_data']['allergies'])} allergies")
        print(f"   ✓ {len(results['ehr_data']['active_medications'])} active medications")
        
        # Step 2: PDMP Check
        print("\nStep 2: Prescription Drug Monitoring Program Check")
        results["pdmp_data"] = self.check_pdmp(patient_id, medication)
        print(f"   ✓ {len(results['pdmp_data']['controlled_substance_history'])} recent controlled substances")
        if results['pdmp_data']['risk_flags']:
            print(f"   ⚠️  Risk flags: {', '.join(results['pdmp_data']['risk_flags'])}")
        
        # Step 3: Insurance Verification
        print("\nStep 3: Insurance Coverage Verification")
        results["insurance_data"] = self.verify_insurance(patient_id, prescription_data)
        print(f"   ✓ Coverage: {results['insurance_data']['coverage_status']}")
        print(f"   💰 Copay: ${results['insurance_data']['copay_amount']}")
        
        # Step 4: Inventory Check
        print("\nStep 4: Inventory Availability Check")
        quantity = int(prescription_data.get('duration', '30 days').split()[0])
        results["inventory_data"] = self.check_inventory(medication, quantity)
        print(f"   {'✓' if results['inventory_data']['in_stock'] else '⚠️ '} Stock: {results['inventory_data']['current_stock']} units")
        
        # Step 5: Send to PMS if blockchain approved
        if blockchain_hash:
            print("\nStep 5: Pharmacy Management System Submission")
            results["pms_data"] = self.send_to_pms(prescription_data, blockchain_hash)
            print(f"   ✓ Order ID: {results['pms_data']['pms_order_id']}")
            print(f"   ⏰ Ready: {results['pms_data']['estimated_ready_time'][:16]}")
        
        print(f"\n{'='*70}\n")
        return results
    
    def _log_integration(self, system: str, action: str, entity_id: str, status: str):
        """Log integration events for audit trail."""
        self.integration_log.append({
            "timestamp": datetime.now().isoformat(),
            "system": system,
            "action": action,
            "entity_id": entity_id,
            "status": status
        })
    
    def get_integration_stats(self) -> Dict:
        """Get statistics on external system integrations."""
        stats = {
            "total_integrations": len(self.integration_log),
            "by_system": defaultdict(int),
            "by_status": defaultdict(int)
        }
        
        for log in self.integration_log:
            stats["by_system"][log["system"]] += 1
            stats["by_status"][log["status"]] += 1
        
        return {
            "total_integrations": stats["total_integrations"],
            "by_system": dict(stats["by_system"]),
            "by_status": dict(stats["by_status"])
        }


# ============================================================================
# PART 8: DASHBOARD UI (Text-based Mockup)
# ============================================================================

class DashboardUI:
    """
    Text-based dashboard interface for the prescription tracking system.
    
    In production, this would be a web-based UI using React/Vue/Angular.
    This mockup demonstrates the UI structure and data flow.
    """
    
    def __init__(self, system):
        """Initialize dashboard with reference to main system."""
        self.system = system
    
    def render_main_dashboard(self):
        """Render the main dashboard overview."""
        print("\n" + "="*80)
        print(" "*25 + "🏥 PRESCRIPTION TRACKING DASHBOARD")
        print("="*80)
        
        # Header with real-time stats
        stats = self.system.get_statistics()
        queue_status = self.system.review_queue.get_queue_status()
        
        print(f"\n{'─'*80}")
        print("📊 REAL-TIME SYSTEM STATUS")
        print(f"{'─'*80}")
        
        # Create a visual status bar
        total = stats['total_prescriptions']
        warnings = stats['prescriptions_with_warnings']
        in_queue = queue_status['total_in_queue']
        
        print(f"""
┌─────────────────────────────────────────────────────────────────────────────┐
│ Total Prescriptions: {total:>3}  │  Warnings: {warnings:>3}  │  In Review Queue: {in_queue:>3}      │
│ Blockchain Status: {'✅ VALID' if stats['blockchain_valid'] else '❌ INVALID':>10} │  SLA Violations: {queue_status['sla_violations']:>3}                    │
└─────────────────────────────────────────────────────────────────────────────┘
        """)
        
        # Quick action buttons (simulated)
        print(f"\n{'─'*80}")
        print("🎯 QUICK ACTIONS")
        print(f"{'─'*80}")
        print("""
[1] Submit New Prescription    [2] Review Queue          [3] View Blockchain
[4] Performance Metrics        [5] Alert History         [6] Integration Status
[7] Generate Report            [8] System Settings       [9] Help
        """)
    
    def render_queue_dashboard(self):
        """Render the review queue dashboard."""
        print("\n" + "="*80)
        print(" "*30 + "📋 REVIEW QUEUE DASHBOARD")
        print("="*80)
        
        queue_items = self.system.review_queue.get_queue_items()
        
        if not queue_items:
            print("\n✅ No items in review queue - all clear!")
            return
        
        # Group by priority
        critical = [item for item in queue_items if item['priority'] == 1]
        high = [item for item in queue_items if item['priority'] == 2]
        moderate = [item for item in queue_items if item['priority'] == 3]
        
        print(f"\n🔴 CRITICAL ({len(critical)})")
        print("─" * 80)
        for item in critical:
            self._render_queue_item(item)
        
        print(f"\n🟠 HIGH ({len(high)})")
        print("─" * 80)
        for item in high:
            self._render_queue_item(item)
        
        print(f"\n🟡 MODERATE ({len(moderate)})")
        print("─" * 80)
        for item in moderate:
            self._render_queue_item(item)
    
    def _render_queue_item(self, item: Dict):
        """Render a single queue item."""
        status_icon = {
            "pending": "⏳",
            "under_review": "👁️ ",
            "approved": "✅",
            "rejected": "❌"
        }.get(item['status'], "❓")
        
        time_in_queue = (datetime.now() - datetime.fromisoformat(item['added_timestamp'])).total_seconds() / 60
        
        print(f"""
┌─ {item['queue_id']} ──────────────────────────────────────────────────────┐
│ {status_icon} Status: {item['status']:<15} │ Risk: {item['risk_assessment']['risk_score']}/100
│ 👤 Patient: {item['prescription_data']['patient_name']:<30}
│ 💊 Medication: {item['prescription_data']['medication']:<25}
│ ⏱️  In Queue: {int(time_in_queue)} minutes │ SLA: {item['sla_deadline'][11:16]}
│ 👨‍⚕️ Assigned: {item.get('assigned_to', 'Unassigned'):<30}
└───────────────────────────────────────────────────────────────────────────┘
        """)
    
    def render_blockchain_explorer(self):
        """Render blockchain visualization."""
        print("\n" + "="*80)
        print(" "*28 + "⛓️  BLOCKCHAIN EXPLORER")
        print("="*80)
        
        chain = self.system.blockchain.chain
        
        for i, block in enumerate(chain[-5:]):  # Show last 5 blocks
            if block.index == 0:
                print(f"\n┌─ Block #0 (Genesis) ─────────────────────────────────────┐")
                print(f"│ Hash: {block.hash[:50]}... │")
                print(f"└──────────────────────────────────────────────────────────┘")
                print("   │")
                print("   ▼")
            else:
                print(f"\n┌─ Block #{block.index} ────────────────────────────────────────────────┐")
                print(f"│ Patient: {block.prescription_data.get('patient_name', 'N/A'):<30}")
                print(f"│ Medication: {block.prescription_data.get('medication', 'N/A'):<25}")
                print(f"│ Hash: {block.hash[:45]}...")
                print(f"│ Prev Hash: {block.previous_hash[:42]}...")
                print(f"│ Time: {block.timestamp[:19]}")
                warning = " ⚠️ WARNING FLAG" if block.prescription_data.get('_warning_flag') else ""
                print(f"│ Status: Valid{warning}")
                print(f"└─────────────────────────────────────────────────────────────┘")
                if i < len(chain[-5:]) - 1:
                    print("   │")
                    print("   ▼")

class PrescriptionValidator:
    """
    Simulates an LLM-based prescription validator.
    
    In a real implementation, this would call Claude API or another LLM
    to analyze prescription safety, drug interactions, and completeness.
    
    Example of real LLM integration:
    
    import anthropic
    
    client = anthropic.Anthropic(api_key="your-api-key")
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{
            "role": "user",
            "content": f"Analyze this prescription for safety: {prescription}"
        }]
    )
    """
    
    # Common drug interactions database (simplified)
    DRUG_INTERACTIONS = {
        "Warfarin": ["Aspirin", "Ibuprofen", "NSAIDs"],
        "MAOIs": ["SSRIs", "Tyramine-rich foods"],
        "Metformin": ["Alcohol", "Iodinated contrast"],
        "Statins": ["Grapefruit juice", "Fibrates"],
        "ACE Inhibitors": ["Potassium supplements", "NSAIDs"],
        "Digoxin": ["Diuretics", "Calcium channel blockers"]
    }
    
    @staticmethod
    def validate_prescription(prescription: Dict) -> Dict:
        """
        Validate prescription data using AI analysis.
        
        Performs multiple validation checks:
        1. Required fields presence
        2. Dosage format validation
        3. Drug interaction checking
        4. Safety recommendations
        
        Args:
            prescription: Dictionary containing prescription data
            
        Returns:
            dict: Validation report with results and recommendations
        """
        validation_result = {
            "is_valid": True,
            "confidence": 0.95,
            "checks_performed": [],
            "warnings": [],
            "recommendations": [],
            "errors": []
        }
        
        # ========== Check 1: Required Fields ==========
        required_fields = [
            "patient_id", 
            "patient_name", 
            "medication", 
            "dosage", 
            "doctor_id", 
            "doctor_name"
        ]
        missing_fields = [f for f in required_fields if f not in prescription]
        
        if missing_fields:
            validation_result["is_valid"] = False
            validation_result["errors"].append(
                f"Missing required fields: {', '.join(missing_fields)}"
            )
            validation_result["checks_performed"].append(
                "✗ Required fields check FAILED"
            )
        else:
            validation_result["checks_performed"].append(
                "✓ All required fields present"
            )
        
        # ========== Check 2: Dosage Format Validation ==========
        if "dosage" in prescription:
            dosage = prescription["dosage"]
            if any(char.isdigit() for char in dosage):
                validation_result["checks_performed"].append(
                    f"✓ Dosage format valid: {dosage}"
                )
            else:
                validation_result["warnings"].append(
                    "⚠ Dosage format unclear - verify with prescribing physician"
                )
                validation_result["checks_performed"].append(
                    "⚠ Dosage format needs verification"
                )
        
        # ========== Check 3: Drug Interaction Check ==========
        if "medication" in prescription:
            medication = prescription["medication"]
            interactions_found = []
            
            for drug, interactions in PrescriptionValidator.DRUG_INTERACTIONS.items():
                if drug.lower() in medication.lower():
                    interactions_found.append({
                        "drug": drug,
                        "interactions": interactions
                    })
                    validation_result["warnings"].append(
                        f"⚠ INTERACTION ALERT: {drug} - verify no concurrent use of {', '.join(interactions)}"
                    )
            
            if interactions_found:
                validation_result["checks_performed"].append(
                    f"⚠ Found {len(interactions_found)} potential interaction(s)"
                )
            else:
                validation_result["checks_performed"].append(
                    "✓ No known drug interactions detected"
                )
        
        # ========== Check 4: Patient Age Validation ==========
        if "patient_age" in prescription:
            age = prescription["patient_age"]
            if age < 18:
                validation_result["warnings"].append(
                    "⚠ Pediatric patient - verify dosage is age-appropriate"
                )
            elif age > 65:
                validation_result["warnings"].append(
                    "⚠ Geriatric patient - monitor for adverse effects and adjust dosage if needed"
                )
        
        # ========== Check 5: Duration Validation ==========
        if "duration" in prescription:
            duration = prescription["duration"]
            if "30" in duration or "month" in duration.lower():
                validation_result["recommendations"].append(
                    "📋 Standard 30-day supply - schedule follow-up appointment"
                )
            elif "90" in duration:
                validation_result["recommendations"].append(
                    "📋 Extended 90-day supply - ensure patient has stable condition"
                )
        
        # ========== General Safety Recommendations ==========
        validation_result["recommendations"].extend([
            "🔍 Verify patient allergy history before dispensing",
            "🆔 Confirm patient identification at pickup",
            "📞 Provide patient counseling on proper medication use"
        ])
        
        # ========== Calculate Confidence Score ==========
        if not validation_result["is_valid"]:
            validation_result["confidence"] = 0.0
        elif validation_result["warnings"]:
            validation_result["confidence"] = 0.75
        elif validation_result["errors"]:
            validation_result["confidence"] = 0.0
        
        # Add metadata
        validation_result["timestamp"] = datetime.now().isoformat()
        validation_result["validated_by"] = "LLM Prescription Validator v1.0"
        validation_result["validation_method"] = "Simulated AI Analysis"
        
        return validation_result


# ============================================================================
# PART 3: PRESCRIPTION MANAGEMENT SYSTEM
# ============================================================================

class PrescriptionTrackingSystem:
    """
    Main system integrating blockchain and LLM validation.
    
    This class orchestrates the entire prescription tracking workflow:
    1. Receive prescription submission
    2. Validate using LLM
    3. Store validated prescriptions in blockchain
    4. Provide query and reporting capabilities
    """
    
    def __init__(self):
        """Initialize the tracking system with blockchain and validator."""
        print("\n" + "="*70)
        print("INITIALIZING PRESCRIPTION TRACKING SYSTEM")
        print("="*70)
        self.blockchain = PrescriptionBlockchain()
        self.validator = PrescriptionValidator()
        self.misuse_predictor = MisusePredictionModel()
        self.alert_system = AlertNotificationSystem()
        self.review_queue = ReviewQueue()
        self.escalation_workflow = EscalationWorkflow(self.alert_system, self.review_queue)
        self.performance_metrics = PerformanceMetrics()
        self.pharmacy_integration = PharmacySystemIntegration()
        self.dashboard = DashboardUI(self)
        self.pdf_exporter = PDFExporter(self)
        print("✓ Blockchain initialized")
        print("✓ Validator initialized")
        print("✓ Misuse prediction model initialized")
        print("✓ Alert & notification system initialized")
        print("✓ Review queue system initialized")
        print("✓ Escalation workflow initialized")
        print("✓ Performance metrics tracker initialized")
        print("✓ Pharmacy system integration initialized")
        print("✓ Dashboard UI initialized")
        print("✓ PDF export system initialized")
        print("✓ System ready")
    
    def submit_prescription(self, prescription_data: Dict) -> Dict:
        """
        Submit a new prescription for validation and blockchain storage.
        
        Workflow:
        1. Validate prescription using LLM
        2. If valid, add to blockchain
        3. Return submission result
        
        Args:
            prescription_data: Dictionary containing prescription information
            
        Returns:
            dict: Result of submission with status and details
        """
        start_time = time.time()
        
        print(f"\n{'='*70}")
        print("PROCESSING NEW PRESCRIPTION")
        print(f"{'='*70}")
        print(f"Patient: {prescription_data.get('patient_name', 'Unknown')}")
        print(f"Medication: {prescription_data.get('medication', 'Unknown')}")
        
        # Step 1: LLM Validation
        print("\n[STEP 1] Running AI validation...")
        val_start = time.time()
        validation_report = self.validator.validate_prescription(prescription_data)
        val_time = time.time() - val_start
        self.performance_metrics.record_validation(val_time)
        
        print(f"\n  Validation Status: {'✓ APPROVED' if validation_report['is_valid'] else '✗ REJECTED'}")
        print(f"  Confidence Score: {validation_report['confidence']:.1%}")
        print(f"\n  Checks Performed:")
        for check in validation_report['checks_performed']:
            print(f"    {check}")
        
        if validation_report['warnings']:
            print(f"\n  ⚠ Warnings:")
            for warning in validation_report['warnings']:
                print(f"    {warning}")
        
        if validation_report['errors']:
            print(f"\n  ✗ Errors:")
            for error in validation_report['errors']:
                print(f"    {error}")
        
        # Step 1.5: Misuse Risk Prediction
        print("\n[STEP 1.5] Running misuse risk analysis...")
        patient_history = self.blockchain.get_patient_history(
            prescription_data.get('patient_id', '')
        )
        misuse_risk = self.misuse_predictor.predict_misuse_risk(
            patient_history, prescription_data
        )
        
        print(f"\n  Risk Level: {misuse_risk['risk_level']}")
        print(f"  Risk Score: {misuse_risk['risk_score']}/100")
        
        if misuse_risk['risk_factors']:
            print(f"\n  Risk Factors:")
            for factor in misuse_risk['risk_factors']:
                print(f"    {factor}")
        
        if misuse_risk['recommendations']:
            print(f"\n  Recommendations:")
            for rec in misuse_risk['recommendations'][:3]:  # Show first 3
                print(f"    {rec}")
        
        # Add misuse risk to validation report
        validation_report['misuse_risk'] = misuse_risk
        
        # Step 2: Risk-based Decision (Flagging System)
        print("\n[STEP 2] Risk-based decision making...")
        
        # Check if prescription should be flagged
        should_flag = (
            not validation_report["is_valid"] or 
            misuse_risk['risk_level'] == "HIGH RISK"
        )
        
        if should_flag:
            # HIGH RISK - RAISE ALERT, DO NOT ADD TO BLOCKCHAIN
            print("\n  🚨 ALERT: PRESCRIPTION FLAGGED FOR REVIEW")
            print("  " + "="*66)
            
            if not validation_report["is_valid"]:
                print("  Reason: Failed validation checks")
            if misuse_risk['risk_level'] == "HIGH RISK":
                print(f"  Reason: High misuse risk (Score: {misuse_risk['risk_score']}/100)")
            
            print("\n  ⛔ PRESCRIPTION NOT ADDED TO BLOCKCHAIN")
            print("  ⚠️  Manual review required by authorized personnel")
            print("  📞 Contact prescribing physician for verification")
            print("  📋 Document all findings in patient file")
            
            # Send alerts via all channels
            alert_level = "CRITICAL" if misuse_risk['risk_score'] >= 80 else "HIGH"
            alert_start = time.time()
            alert_record = self.alert_system.send_alert(
                alert_level, prescription_data, misuse_risk, 
                {"status": "flagged"}
            )
            alert_time = time.time() - alert_start
            self.performance_metrics.record_alert(alert_time)
            
            # Add to review queue
            queue_item = self.review_queue.add_to_queue(
                prescription_data, misuse_risk, validation_report, alert_level
            )
            
            print(f"\n  📋 Added to review queue: {queue_item['queue_id']}")
            print(f"  ⏰ SLA Deadline: {queue_item['sla_deadline'][:16]}")
            
            processing_time = time.time() - start_time
            self.performance_metrics.record_prescription_processing(processing_time, False)
            
            result = {
                "status": "flagged",
                "message": "Prescription flagged for manual review - NOT added to blockchain",
                "flagged": True,
                "requires_review": True,
                "validation_report": validation_report,
                "alert_level": alert_level,
                "alert_id": alert_record["alert_id"],
                "queue_id": queue_item["queue_id"],
                "processing_time_ms": round(processing_time * 1000, 2)
            }
            
        elif misuse_risk['risk_level'] == "MODERATE RISK":
            # MODERATE RISK - ADD WITH WARNING FLAG
            print("\n  ⚠️  CAUTION: Moderate risk detected")
            print("  Adding to blockchain with warning flag...")
            
            # Add warning flag to prescription data
            prescription_data['_warning_flag'] = True
            prescription_data['_risk_level'] = "MODERATE"
            
            bc_start = time.time()
            block = self.blockchain.add_block(prescription_data, validation_report)
            bc_time = time.time() - bc_start
            self.performance_metrics.record_blockchain_write(bc_time)
            
            print(f"  ✓ Block #{block.index} created WITH WARNING FLAG")
            print(f"  Block Hash: {block.hash[:32]}...")
            print(f"  ⚠️  Enhanced monitoring recommended")
            
            # Run external system integration
            integration_result = self.pharmacy_integration.full_integration_workflow(
                prescription_data, block.hash
            )
            
            processing_time = time.time() - start_time
            self.performance_metrics.record_prescription_processing(processing_time, True)
            
            result = {
                "status": "success_with_warning",
                "message": "Prescription added to blockchain with moderate risk warning",
                "block_index": block.index,
                "block_hash": block.hash,
                "flagged": False,
                "warning": True,
                "validation_report": validation_report,
                "integration_result": integration_result,
                "processing_time_ms": round(processing_time * 1000, 2)
            }
            
        else:
            # LOW RISK - ADD NORMALLY
            print("\n  ✓ Low risk - proceeding with blockchain entry...")
            bc_start = time.time()
            block = self.blockchain.add_block(prescription_data, validation_report)
            bc_time = time.time() - bc_start
            self.performance_metrics.record_blockchain_write(bc_time)
            
            print(f"  ✓ Block #{block.index} created successfully")
            print(f"  Block Hash: {block.hash[:32]}...")
            print(f"  Previous Hash: {block.previous_hash[:32]}...")
            
            # Run external system integration
            integration_result = self.pharmacy_integration.full_integration_workflow(
                prescription_data, block.hash
            )
            
            processing_time = time.time() - start_time
            self.performance_metrics.record_prescription_processing(processing_time, True)
            
            result = {
                "status": "success",
                "message": "Prescription validated and added to blockchain",
                "block_index": block.index,
                "block_hash": block.hash,
                "flagged": False,
                "warning": False,
                "validation_report": validation_report,
                "integration_result": integration_result,
                "processing_time_ms": round(processing_time * 1000, 2)
            }
        
        print(f"{'='*70}\n")
        return result
    
    def view_blockchain(self):
        """Display the entire blockchain with all prescriptions."""
        print(f"\n{'='*70}")
        print("BLOCKCHAIN CONTENTS")
        print(f"{'='*70}")
        print(f"Total Blocks: {len(self.blockchain.chain)}")
        print(f"Chain Valid: {'✓ YES' if self.blockchain.is_chain_valid() else '✗ NO'}")
        print(f"{'='*70}")
        
        for block in self.blockchain.chain:
            print(f"\n{'─'*70}")
            print(f"BLOCK #{block.index}")
            print(f"{'─'*70}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            
            if block.index > 0:  # Skip genesis block details
                print(f"\nPrescription Data:")
                print(f"  Patient: {block.prescription_data.get('patient_name')} (ID: {block.prescription_data.get('patient_id')})")
                print(f"  Medication: {block.prescription_data.get('medication')}")
                print(f"  Dosage: {block.prescription_data.get('dosage')}")
                print(f"  Duration: {block.prescription_data.get('duration')}")
                print(f"  Doctor: {block.prescription_data.get('doctor_name')} (ID: {block.prescription_data.get('doctor_id')})")
                
                print(f"\nValidation Report:")
                print(f"  Status: {'✓ Valid' if block.validation_report.get('is_valid') else '✗ Invalid'}")
                print(f"  Confidence: {block.validation_report.get('confidence', 0):.1%}")
                
                if block.validation_report.get('warnings'):
                    print(f"  Warnings: {len(block.validation_report['warnings'])}")
        
        print(f"\n{'='*70}\n")
    
    def get_flagged_prescriptions(self) -> List[Dict]:
        """
        Retrieve all prescriptions that were flagged and not added to blockchain.
        
        Note: In a production system, flagged prescriptions would be stored in
        a separate database/queue for review. This is a simplified implementation.
        
        Returns:
            list: Flagged prescription records (stored in memory during session)
        """
        # This would query a separate flagged prescriptions database
        # For now, we'll return an empty list as flagged items aren't stored
        return []
    
    def get_warning_prescriptions(self) -> List[Dict]:
        """
        Retrieve all prescriptions in blockchain that have warning flags.
        
        Returns:
            list: Prescription records with moderate risk warnings
        """
        return [
            block.to_dict()
            for block in self.blockchain.chain[1:]
            if block.prescription_data.get('_warning_flag', False)
        ]
    
    def view_review_queue(self):
        """Display the current review queue status."""
        print(f"\n{'='*70}")
        print("REVIEW QUEUE STATUS")
        print(f"{'='*70}")
        
        queue_status = self.review_queue.get_queue_status()
        print(f"Pending Reviews: {queue_status['pending']}")
        print(f"Under Review: {queue_status['under_review']}")
        print(f"Total in Queue: {queue_status['total_in_queue']}")
        print(f"Total Reviewed: {queue_status['total_reviewed']}")
        print(f"⚠️  SLA Violations: {queue_status['sla_violations']}")
        
        if queue_status['total_in_queue'] > 0:
            print(f"\n{'─'*70}")
            print("CURRENT QUEUE ITEMS:")
            print(f"{'─'*70}")
            
            for item in self.review_queue.get_queue_items():
                print(f"\nQueue ID: {item['queue_id']}")
                print(f"  Priority: {item['alert_level']}")
                print(f"  Status: {item['status']}")
                print(f"  Patient: {item['prescription_data'].get('patient_name')}")
                print(f"  Medication: {item['prescription_data'].get('medication')}")
                print(f"  Risk Score: {item['risk_assessment'].get('risk_score')}/100")
                print(f"  Added: {item['added_timestamp'][:16]}")
                print(f"  SLA Deadline: {item['sla_deadline'][:16]}")
                if item.get('assigned_to'):
                    print(f"  Assigned To: {item['assigned_to']}")
        
        print(f"\n{'='*70}\n")
    
    def simulate_review_process(self):
        """Simulate the review and approval process."""
        print(f"\n{'='*70}")
        print("SIMULATING REVIEW PROCESS")
        print(f"{'='*70}")
        
        next_item = self.review_queue.get_next_item()
        if next_item:
            print(f"\nReviewing: {next_item['queue_id']}")
            print(f"Patient: {next_item['prescription_data'].get('patient_name')}")
            print(f"Medication: {next_item['prescription_data'].get('medication')}")
            
            # Assign to reviewer
            self.review_queue.assign_to_reviewer(next_item['queue_id'], "Dr. Jane Reviewer")
            print(f"✓ Assigned to: Dr. Jane Reviewer")
            
            # Simulate review decision
            decision = "approved"  # or "rejected"
            notes = "Contacted prescribing physician. Prescription verified as legitimate for chronic pain management."
            
            result = self.review_queue.complete_review(
                next_item['queue_id'],
                decision,
                notes,
                "Dr. Jane Reviewer"
            )
            
            print(f"✓ Review completed: {decision.upper()}")
            print(f"  Review time: {result.get('review_duration_minutes', 0)} minutes")
            print(f"  Notes: {notes}")
        else:
            print("No items in queue to review.")
        
        print(f"{'='*70}\n")
        """
        Generate system statistics.
        
        Returns:
            dict: Statistics about prescriptions in the system
        """
        total_prescriptions = len(self.blockchain.chain) - 1  # Exclude genesis
        
        medications = {}
        doctors = {}
        patients = set()
        
        for block in self.blockchain.chain[1:]:
            med = block.prescription_data.get('medication')
            doc_id = block.prescription_data.get('doctor_id')
            pat_id = block.prescription_data.get('patient_id')
            
            if med:
                medications[med] = medications.get(med, 0) + 1
            if doc_id:
                doctors[doc_id] = doctors.get(doc_id, 0) + 1
            if pat_id:
                patients.add(pat_id)
        
        return {
            "total_prescriptions": total_prescriptions,
            "unique_patients": len(patients),
            "unique_doctors": len(doctors),
            "unique_medications": len(medications),
            "most_prescribed": max(medications.items(), key=lambda x: x[1]) if medications else None,
            "blockchain_valid": self.blockchain.is_chain_valid()
        }


# ============================================================================
# PART 4: DEMONSTRATION & TESTING
# ============================================================================

def print_section_header(title: str):
    """Print a formatted section header."""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def main():
    """Run the prescription tracking system demonstration."""
    
    print_section_header("AI-POWERED BLOCKCHAIN PRESCRIPTION TRACKING SYSTEM")
    print("Demonstration of blockchain + AI for healthcare prescription management")
    print("="*70)
    
    # Initialize system
    system = PrescriptionTrackingSystem()
    
    # ========== TEST CASE 1: Valid Prescription ==========
    print_section_header("TEST CASE 1: Valid Prescription")
    prescription_1 = {
        "patient_id": "P001",
        "patient_name": "John Doe",
        "patient_age": 45,
        "medication": "Lisinopril",
        "dosage": "10mg once daily",
        "duration": "30 days",
        "doctor_id": "D101",
        "doctor_name": "Dr. Sarah Smith",
        "date_prescribed": "2025-11-09"
    }
    result_1 = system.submit_prescription(prescription_1)
    
    # ========== TEST CASE 2: Prescription with Warnings ==========
    print_section_header("TEST CASE 2: High-Risk Controlled Substance")
    prescription_2 = {
        "patient_id": "P002",
        "patient_name": "Jane Smith",
        "patient_age": 62,
        "medication": "Oxycodone",
        "dosage": "30mg twice daily",
        "duration": "30 days",
        "doctor_id": "D102",
        "doctor_name": "Dr. Michael Johnson",
        "date_prescribed": "2025-11-09"
    }
    result_2 = system.submit_prescription(prescription_2)
    
    # ========== TEST CASE 3: Invalid Prescription ==========
    print_section_header("TEST CASE 3: Invalid Prescription (Missing Required Data)")
    prescription_3 = {
        "patient_id": "P003",
        "medication": "Amoxicillin",
        "dosage": "500mg three times daily"
        # Missing: patient_name, doctor_id, doctor_name
    }
    result_3 = system.submit_prescription(prescription_3)
    
    # ========== TEST CASE 4: Pediatric Patient ==========
    print_section_header("TEST CASE 4: Pediatric Patient Prescription")
    prescription_4 = {
        "patient_id": "P004",
        "patient_name": "Tommy Wilson",
        "patient_age": 8,
        "medication": "Amoxicillin",
        "dosage": "250mg three times daily",
        "duration": "10 days",
        "doctor_id": "D103",
        "doctor_name": "Dr. Emily Chen",
        "date_prescribed": "2025-11-09"
    }
    result_4 = system.submit_prescription(prescription_4)
    
    # ========== TEST CASE 5: Potential Doctor Shopping ==========
    print_section_header("TEST CASE 5: Potential Doctor Shopping Pattern")
    # Same patient (P002) getting same medication from different doctor
    prescription_5 = {
        "patient_id": "P002",
        "patient_name": "Jane Smith",
        "patient_age": 62,
        "medication": "Oxycodone",
        "dosage": "30mg twice daily",
        "duration": "30 days",
        "doctor_id": "D104",  # Different doctor!
        "doctor_name": "Dr. Robert Brown",
        "date_prescribed": "2025-11-09"
    }
    result_5 = system.submit_prescription(prescription_5)
    
    # ========== TEST CASE 6: Early Refill Pattern ==========
    print_section_header("TEST CASE 6: Early Refill (Simulated)")
    # Same patient trying to refill too early
    prescription_6 = {
        "patient_id": "P002",
        "patient_name": "Jane Smith",
        "patient_age": 62,
        "medication": "Oxycodone",
        "dosage": "40mg twice daily",  # Increased dosage!
        "duration": "30 days",
        "doctor_id": "D102",
        "doctor_name": "Dr. Michael Johnson",
        "date_prescribed": "2025-11-09"
    }
    result_6 = system.submit_prescription(prescription_6)
    
    # Display blockchain
    system.view_blockchain()
    
    # Verify blockchain integrity
    print_section_header("BLOCKCHAIN INTEGRITY VERIFICATION")
    is_valid = system.blockchain.is_chain_valid()
    print(f"Chain is valid: {'✓ YES' if is_valid else '✗ NO'}")
    print(f"Total blocks in chain: {len(system.blockchain.chain)}")
    print("="*70)
    
    # Query patient history
    print_section_header("PATIENT PRESCRIPTION HISTORY QUERY")
    patient_history = system.blockchain.get_patient_history("P001")
    print(f"\nPrescriptions for Patient P001 (John Doe): {len(patient_history)}")
    for record in patient_history:
        print(f"  • {record['prescription_data']['medication']} - "
              f"{record['prescription_data']['dosage']} - "
              f"Prescribed on {record['timestamp'][:10]}")
    
    # System statistics
    print_section_header("SYSTEM STATISTICS")
    stats = system.get_statistics()
    print(f"Total Prescriptions: {stats['total_prescriptions']}")
    print(f"Unique Patients: {stats['unique_patients']}")
    print(f"Unique Doctors: {stats['unique_doctors']}")
    print(f"Unique Medications: {stats['unique_medications']}")
    print(f"⚠️  Prescriptions with Warnings: {stats['prescriptions_with_warnings']}")
    if stats['most_prescribed']:
        print(f"Most Prescribed: {stats['most_prescribed'][0]} ({stats['most_prescribed'][1]} times)")
    print(f"Blockchain Status: {'✓ Valid' if stats['blockchain_valid'] else '✗ Invalid'}")
    
    # Show warning prescriptions
    print_section_header("PRESCRIPTIONS WITH WARNINGS")
    warning_prescriptions = system.get_warning_prescriptions()
    if warning_prescriptions:
        print(f"Found {len(warning_prescriptions)} prescription(s) with moderate risk warnings:\n")
        for record in warning_prescriptions:
            print(f"  • Patient: {record['prescription_data']['patient_name']}")
            print(f"    Medication: {record['prescription_data']['medication']}")
            print(f"    Risk Level: {record['prescription_data'].get('_risk_level', 'UNKNOWN')}")
            print(f"    Date: {record['timestamp'][:10]}")
            print()
    else:
        print("No prescriptions with warnings in the system.")
    
    # Alert summary
    print_section_header("ALERT SUMMARY")
    print("During this session:")
    print(f"  ✓ Approved and added to blockchain: {stats['total_prescriptions'] - stats['prescriptions_with_warnings']}")
    print(f"  ⚠️  Approved with warnings: {stats['prescriptions_with_warnings']}")
    
    # Get alert history
    alert_history = system.alert_system.get_alert_history()
    critical_alerts = len(system.alert_system.get_alerts_by_level("CRITICAL"))
    high_alerts = len(system.alert_system.get_alerts_by_level("HIGH"))
    
    print(f"  🚨 Critical alerts sent: {critical_alerts}")
    print(f"  ⚠️  High alerts sent: {high_alerts}")
    print(f"  📧 Total notifications: {len(alert_history)}")
    print("\nNote: Flagged prescriptions are held in review queue and not added to blockchain.")
    print("They require manual approval by authorized personnel before processing.")
    
    # Display review queue
    system.view_review_queue()
    
    # Simulate review process
    system.simulate_review_process()
    
    # Check for escalations
    print_section_header("ESCALATION CHECK")
    escalations = system.escalation_workflow.check_escalations()
    if escalations:
        print(f"Found {len(escalations)} item(s) requiring escalation:\n")
        for esc in escalations:
            print(f"  • Queue ID: {esc['queue_id']}")
            print(f"    Reason: {esc['reason']}")
            print(f"    Escalated: {esc['original_level']} → {esc['escalated_to']}")
    else:
        print("✓ No escalations needed at this time.")
    
    # Performance Metrics
    system.performance_metrics.print_performance_report()
    
    # Integration Statistics
    print_section_header("EXTERNAL SYSTEM INTEGRATION STATISTICS")
    integration_stats = system.pharmacy_integration.get_integration_stats()
    print(f"Total Integration Calls: {integration_stats['total_integrations']}")
    print(f"\nBy System:")
    for system_name, count in integration_stats['by_system'].items():
        print(f"  • {system_name}: {count} calls")
    print(f"\nStatus:")
    for status, count in integration_stats['by_status'].items():
        print(f"  • {status}: {count}")
    
    # Dashboard UI Demonstrations
    print_section_header("DASHBOARD UI DEMONSTRATIONS")
    print("\n1. Main Dashboard:")
    system.dashboard.render_main_dashboard()
    
    print("\n\n2. Review Queue Dashboard:")
    system.dashboard.render_queue_dashboard()
    
    print("\n\n3. Blockchain Explorer:")
    system.dashboard.render_blockchain_explorer()
    
    # PDF Report Generation
    print_section_header("PDF REPORT GENERATION")
    print("Generating comprehensive PDF reports for compliance and auditing...\n")
    
    # Generate all reports
    reports = system.pdf_exporter.export_all_reports("./prescription_reports")
    
    print("\n📁 Generated Reports:")
    for report_type, filepath in reports.items():
        print(f"   • {report_type.replace('_', ' ').title()}: {filepath}")
    
    print("\n" + "="*70)
    print("💡 TIP: Open the HTML files in your browser to view the reports")
    print("   For production, install WeasyPrint to generate actual PDFs:")
    print("   pip install weasyprint")
    print("="*70)
    
    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)
    print("\nNext Steps:")
    print("1. Review the blockchain structure and validation reports")
    print("2. Complete the assignment tasks to enhance the system")
    print("3. Integrate with real LLM API (Claude, OpenAI, etc.)")
    print("4. Add encryption for sensitive patient data")
    print("5. Build a web interface for easier interaction")
    print("6. Review generated PDF reports in ./prescription_reports/")
    print("7. Install PDF library for production: pip install weasyprint")
    print("="*70 + "\n")


# ============================================================================
# ASSIGNMENT TASKS FOR STUDENTS
# ============================================================================

"""
STUDENT TASKS:
=============

TASK 1: Enhance LLM Integration (15 points)
--------------------------------------------
Replace the simulated validator with actual Claude API calls.

Steps:
1. Install anthropic package: pip install anthropic
2. Set up API key: export ANTHROPIC_API_KEY='your-key'
3. Modify PrescriptionValidator.validate_prescription() to use real API
4. Parse LLM response and extract validation insights
5. Handle API errors gracefully

Example code:
```python
import anthropic

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    messages=[{
        "role": "user",
        "content": f"Analyze this prescription for safety: {json.dumps(prescription)}"
    }]
)
```


TASK 2: Add Comprehensive Drug Interaction Database (15 points)
---------------------------------------------------------------
Create a more extensive drug interaction checker.

Requirements:
- Expand DRUG_INTERACTIONS dictionary with at least 20 medications
- Add severity levels (critical, moderate, minor)
- Include food and supplement interactions
- Use LLM to analyze complex multi-drug interactions


TASK 3: Implement Patient Privacy & Security (20 points)
--------------------------------------------------------
Add encryption and access control.

Requirements:
- Encrypt sensitive patient data before blockchain storage
- Implement role-based access control (doctor, pharmacist, patient, admin)
- Create audit logs for all data access
- Add digital signatures for prescriptions


TASK 4: Smart Contract Logic (20 points)
----------------------------------------
Add prescription lifecycle management.

Requirements:
- Track prescription expiration dates
- Implement refill limits (e.g., max 3 refills)
- Create automated alerts for expiring prescriptions
- Add prescription cancellation/modification workflow


TASK 5: Advanced Query & Reporting (15 points)
----------------------------------------------
Enhance data retrieval capabilities.

Requirements:
- Implement full-text search across all prescriptions
- Add date range filtering
- Create statistical reports (most prescribed drugs, prescribing patterns)
- Generate doctor performance analytics
- Export data to CSV/JSON


TASK 6: Web Interface (15 points)
---------------------------------
Build a user-friendly web application.

Requirements:
- Use Flask or FastAPI framework
- Create forms for prescription submission
- Display blockchain visually (timeline or graph)
- Add real-time validation feedback
- Implement user authentication


TASK 7: PDF Reporting System (COMPLETED) ✅
-------------------------------------------
Export system data to professional PDF reports.

Features already implemented:
- Prescription validation reports with risk assessment
- Blockchain audit trail reports
- Performance metrics reports  
- Compliance reports for regulatory requirements
- Alert summary reports
- Batch export functionality

To use in production:
```python
# Install PDF library
pip install weasyprint

# Generate reports
system.pdf_exporter.generate_blockchain_audit_report("audit.pdf")
system.pdf_exporter.generate_performance_report("performance.pdf")
system.pdf_exporter.generate_compliance_report(start_date, end_date, "compliance.pdf")
system.pdf_exporter.export_all_reports("./reports")
```


BONUS TASK: Multi-node Distributed Blockchain (+10 points)
---------------------------------------------------------
Implement distributed consensus.

Requirements:
- Create multiple validator nodes
- Implement proof-of-stake or proof-of-authority consensus
- Handle network synchronization
- Test Byzantine fault tolerance


GRADING RUBRIC:
--------------
- Code quality and documentation: 20%
- Functionality and completeness: 40%
- Error handling and edge cases: 20%
- Innovation and extra features: 20%

Total: 100 points + 10 bonus points possible
"""


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
